import re
from numbers import Number
from . import models
from . import requester

class Clayful:

	base_url = 'https://api.clayful.io'

	default_headers = {
		'Accept-Encoding': 'gzip',
		'X-Clayful-SDK':   'clayful-python'
	}

	plugins = {
		'request': requester.request
	}

	@staticmethod
	def options_to_headers(o = {}):

		headers = {};

		if 'language' in o:
			headers['Accept-Language'] = o['language'];

		if 'currency' in o:
			headers['Accept-Currency'] = o['currency'];

		if 'time_zone' in o:
			headers['Accept-Time-Zone'] = o['time_zone'];

		if 'client' in o:
			headers['Authorization'] = 'Bearer ' + o['client'];

		if 'customer' in o:
			headers['X-Clayful-Customer-Authorization'] = 'Bearer ' + o['customer'];

		if 'error_language' in o:
			headers['X-Clayful-Error-Language'] = o['error_language'];

		if 'headers' in o:
			headers.update(o['headers'])

		return headers


	@staticmethod
	def get_endpoint(path):

		return Clayful.base_url + path

	@staticmethod
	def normalize_query_values(query = {}):

		copied = query.copy()

		for key in copied:

			if isinstance(copied[key], bool):

				copied[key] = 'true' if copied[key] == True else 'false'

			if isinstance(copied[key], Number):

				copied[key] = str(copied[key])

		return copied


	@staticmethod
	def extract_request_arguments(options):

		result = {
			'http_method': options['http_method'],
			'request_url': options['path'],
			'payload':     None,
			'query':       {},
			'headers':     {}
		}

		rest = options['args'][len(options['params']):]

		for i, key in enumerate(options['params']):

			result['request_url'] = result['request_url'].replace('{' + key + '}', str(options['args'][i]))

		if (options['http_method'] == 'POST' or options['http_method'] == 'PUT') and (options.get('without_payload', False) == False):

			result['payload'] = rest[0]
			rest = rest[1:]

		query_headers = {}

		try:
			query_headers = rest[0]

		except IndexError:
			query_headers = {}

		result['query'] = Clayful.normalize_query_values(query_headers.get('query', {}))
		result['headers'] = Clayful.options_to_headers(query_headers)

		return result


	@staticmethod
	def call_api(options):

		extracted = Clayful.extract_request_arguments(options)
		extracted.update({
			'request_url':    Clayful.get_endpoint(extracted['request_url']),
			'model_name':     options['model_name'],
			'method_name':    options['method_name'],
			'uses_form_data': options.get('uses_form_data', False)
		})

		default_headers = Clayful.default_headers.copy()

		default_headers.update(extracted['headers'])

		extracted['headers'] = default_headers

		return Clayful.plugins['request'](extracted)


	@staticmethod
	def config(options = {}):

		headers = Clayful.options_to_headers(options)

		Clayful.default_headers.update(headers)


	@staticmethod
	def install(scope, plugin):

		if scope in Clayful.plugins:

			Clayful.plugins[scope] = plugin

	@staticmethod
	def format_image_url(base_url, options = {}):

		query = []

		normalized = Clayful.normalize_query_values(options)

		for key in normalized:

			query.append(key + '=' + normalized.get(key, ''))

		query = '&'.join(query)

		if bool(query):

			query = '?' + query

		return base_url + query


	@staticmethod
	def format_number(number, currency = {}):

		if not isinstance(number, Number):

			return ''

		precision = currency.get('precision', None)
		delimiter = currency.get('delimiter', {})
		thousands = delimiter.get('thousands', '')
		decimal = delimiter.get('decimal', '.')

		if isinstance(precision, Number):

			n = 10 ** precision
			number = round(number * n) / n

			# To deal with 0.0 case..
			if precision == 0:
				number = int(number)

		parts = str(number).split('.')


		a = thousands.join(re.findall('.{1,3}', parts[0][::-1]))[::-1]
		b = parts[1] if len(parts) > 1 else ''

		if isinstance(precision, Number):

			diff = precision - len(b)
			diff = 0 if diff < 0 else diff;

			b += '0' * diff

		decimal = decimal if bool(b) else ''

		return decimal.join([a, b])


	@staticmethod
	def format_price(number, currency = {}):

		formatted_number = Clayful.format_number(number, currency)

		if not bool(formatted_number):

			return ''

		symbol = currency.get('symbol', '')
		format = currency.get('format', '{price}')

		return format.replace('{symbol}', symbol).replace('{price}', formatted_number)


# Register models
models.register(Clayful)