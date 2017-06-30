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

		result['query'] = query_headers.get('query', {})
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


# Register models
models.register(Clayful)