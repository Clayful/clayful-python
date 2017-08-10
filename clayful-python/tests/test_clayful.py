import unittest
from clayful import Clayful

# Define mock requester class for tests
class MockRequester():

	def __init__(self):

		self.requests = []

	def request(self, request_option):

		self.requests = self.requests + [request_option]


class ClayfulMainModuleTest(unittest.TestCase):

	def test__default_options_for_api_client(self):

		self.assertEqual(Clayful.base_url, 'https://api.clayful.io')
		self.assertEqual(Clayful.default_headers, {
			'Accept-Encoding': 'gzip',
			'X-Clayful-SDK':   'clayful-python'
		})
		self.assertTrue(callable(Clayful.plugins['request']))
		self.assertEqual(str(type(Clayful.Brand)), "<type 'classobj'>")
		self.assertEqual(Clayful.Brand.Clayful, Clayful)


	def test_options_to_headers(self):

		result1 = Clayful.options_to_headers({})
		result2 = Clayful.options_to_headers({
			'language':       'ko',
			'currency':       'KRW',
			'time_zone':      'Asia/Seoul',
			'client':         'client_token',
			'customer':       'customer_token',
			'error_language': 'ko',
			'headers':        {
				'X-Extra': 'Extra'
			}
		})

		self.assertEqual(result1, {})
		self.assertEqual(result2, {
			'Accept-Language':                  'ko',
			'Accept-Currency':                  'KRW',
			'Accept-Time-Zone':                 'Asia/Seoul',
			'Authorization':                    'Bearer client_token',
			'X-Clayful-Customer-Authorization': 'Bearer customer_token',
			'X-Clayful-Error-Language':         'ko',
			'X-Extra':                          'Extra'
		})


	def test_get_api_endpoint(self):

		self.assertEqual(Clayful.get_endpoint('/v1/products'), Clayful.base_url + '/v1/products')


	def test_extract_api_request_arguments(self):

		def build_get_delete_test_cases(method):

			return [
				{
					'options': {
						'http_method': method,
						'path':        '/v1/products', # no params
						'params':      (),
						'args':        () # no args
					},
					'result':   {
						'http_method': method,
						'request_url': '/v1/products',
						'payload':     None,
						'query':       {},
						'headers':     {},
					}
				},
				{
					'options':  {
						'http_method': method,
						'path':        '/v1/products/{productId}',
						'params':      ('productId', ),
						'args':        (
							'pid', # param1
							{      # queryHeaders
								'query':    { 'raw': True, 'originalPrice>': 1000, 'type': 'custom' },
								'language': 'en'
							},
						)
					},
					'result':   {
						'http_method': method,
						'request_url': '/v1/products/pid',
						'payload':     None,
						'query':       { 'raw': 'true', 'originalPrice>': '1000', 'type': 'custom' }, # stringified values
						'headers':     { 'Accept-Language': 'en' },
					}
				},
			]


		def build_post_put_test_cases(method):

			return [
				{
					'options':  {
						'http_method': method,
						'path':        '/v1/store', # no params
						'params':      (),
						'args':        (
							{ 'slug': 'new-slug' },  # payload
						)
					},
					'result':   {
						'http_method': method,
						'request_url': '/v1/store',
						'payload':     { 'slug': 'new-slug' },
						'query':       {},
						'headers':     {},
					}
				},
				{
					'options':  {
						'http_method': method,
						'path':        '/v1/products/{productId}',
						'params':      ('productId', ),
						'args':        (
							'pid', # param1
							{      # payload
								'slug': 'new-slug'
							},
							{      # queryHeaders
								'query':    { 'raw': True },
								'language': 'en'
							},
						)
					},
					'result':   {
						'http_method': method,
						'request_url': '/v1/products/pid',
						'payload':     { 'slug': 'new-slug' },
						'query':       { 'raw': 'true' }, # stringified values
						'headers':     { 'Accept-Language': 'en' },
					}
				},
				{
					'options':  {
						'http_method':     method,
						'path':            '/v1/me/products/reviews/{reviewId}/flag',
						'params':          ('reviewId', ),
						'without_payload': True, # no payload
						'args':            (
							'rid', # param1
							{      # queryHeaders
								'query':     { 'raw': True },
								'language':  'en'
							},
						)
					},
					'result':   {
						'http_method': method,
						'request_url': '/v1/me/products/reviews/rid/flag',
						'payload':     None,
						'query':       { 'raw': 'true' }, # stringified values
						'headers':     { 'Accept-Language': 'en' },
					}
				},
			]

		cases = build_get_delete_test_cases('GET') + build_get_delete_test_cases('DELETE') + build_post_put_test_cases('POST') + build_post_put_test_cases('PUT')

		for c in cases:

			extracted = Clayful.extract_request_arguments(c['options']);

			self.assertEqual(extracted, c['result'])

	def test_call_api(self):

		mock_requester = MockRequester()

		Clayful.install('request', mock_requester.request)

		Clayful.call_api({
			'model_name':     'Brand',
			'method_name':    'query',
			'http_method':    'GET',
			'path':           '/v1/brands',
			'params':         (),
			'args':           ({ 'currency': 'KRW' }, )
		})

		Clayful.call_api({
			'model_name':     'Image',
			'method_name':    'create',
			'http_method':    'POST',
			'path':           '/v1/images',
			'params':         (),
			'uses_form_data': True,
			'args':           (
				{ 'file': 'file' },
				{ 'language': 'ko' },
			)
		})

		self.assertEqual(Clayful.default_headers, {
			'Accept-Encoding': 'gzip',
			'X-Clayful-SDK':   'clayful-python'
		})

		self.assertEqual(mock_requester.requests[0], {
			'model_name':     'Brand',
			'method_name':    'query',
			'http_method':    'GET',
			'request_url':    Clayful.base_url + '/v1/brands',
			'query':          {},
			'headers':        {
				'Accept-Encoding': 'gzip',
				'Accept-Currency': 'KRW',
				'X-Clayful-SDK':   'clayful-python'
			},
			'payload':        None,
			'uses_form_data': False
		})

		self.assertEqual(mock_requester.requests[1], {
			'model_name':     'Image',
			'method_name':    'create',
			'http_method':    'POST',
			'request_url':    Clayful.base_url + '/v1/images',
			'query':          {},
			'headers':        {
				'Accept-Encoding': 'gzip',
				'Accept-Language': 'ko',
				'X-Clayful-SDK':   'clayful-python'
			},
			'payload':        { 'file': 'file' },
			'uses_form_data': True
		})

		self.assertEqual(Clayful.default_headers, {
			'Accept-Encoding': 'gzip',
			'X-Clayful-SDK':   'clayful-python'
		})


	def test_config_api_client(self):

		Clayful.config({
			'language':       'ko',
			'currency':       'KRW',
			'time_zone':      'Asia/Seoul',
			'client':         'client_token',
			'customer':       'customer_token',
			'error_language': 'ko',
			'headers':        {
				'X-Extra': 'Extra'
			}
		})

		self.assertEqual(Clayful.default_headers, {
			'Accept-Encoding':                  'gzip',
			'Accept-Language':                  'ko',
			'Accept-Currency':                  'KRW',
			'Accept-Time-Zone':                 'Asia/Seoul',
			'Authorization':                    'Bearer client_token',
			'X-Clayful-Customer-Authorization': 'Bearer customer_token',
			'X-Clayful-Error-Language':         'ko',
			'X-Clayful-SDK':                    'clayful-python',
			'X-Extra':                          'Extra'
		})


	def test_install_request_middleware(self):

		def req():
			pass

		Clayful.install('request', req)

		self.assertEqual(Clayful.plugins['request'], req)

	def test_format_image_url(self):

		url = 'http://clayful.io'

		cases = [
			{
				'out':     url
			},
			{
				'out':     url,
				'options': {}
			},
			{
				'out':     url + '?width=120',
				'options': { 'width' : 120 }
			},
			{
				'out':     url + '?width=120&height=120',
				'options': { 'width' : 120, 'height' : 120 }
			}
		]

		for c in cases:

			options = c.get('options', None)

			if options is None:

				self.assertEqual(Clayful.format_image_url(url), c.get('out'))

			else:
				self.assertEqual(Clayful.format_image_url(url, options), c.get('out'))

	def test_format_number(self):

		cases = [
			{
				'in':  None,
				'out': ''
			},
			{
				'in':  0,
				'out': '0'
			},
			{
				'in':  10,
				'out': '10'
			},
			{
				'options': {},
				'in':      10,
				'out':     '10'
			},
			# precision tests
			{
				'in':  0.250,
				'out': '0.25'
			},
			{
				'options': { 'precision' : 0 },
				'in':      0,
				'out':     '0'
			},
			{
				'options': { 'precision' : 0 },
				'in':      1234567.25,
				'out':     '1234567'
			},
			{
				'options': { 'precision' : 1 },
				'in':      1234567.24,
				'out':     '1234567.2' # rounded
			},
			{
				'options': { 'precision' : 1 },
				'in':      1234567.25,
				'out':     '1234567.3' # rounded
			},
			{
				'options': { 'precision' : 2 },
				'in':      1234567.25,
				'out':     '1234567.25'
			},
			{
				'options': { 'precision' : 3 },
				'in':      1234567.25,
				'out':     '1234567.250'
			},
			{
				'options': { 'precision' : 0 },
				'in':      1234567,
				'out':     '1234567'
			},
			{
				'options': { 'precision' : 3 },
				'in':      1234567,
				'out':     '1234567.000'
			},
			# delimiter tests
			{
				'options': {
					'precision': 3
				},
				'in':  1234567.25,
				'out': '1234567.250'
			},
			{
				'options': {
					'precision': 3,
					'delimiter': {}
				},
				'in':  1234567.25,
				'out': '1234567.250'
			},
			{
				'options': {
					'precision': 3,
					'delimiter': {
						'thousands': ','
					}
				},
				'in':  1234567.25,
				'out': '1,234,567.250'
			},
			{
				'options': {
					'precision': 3,
					'delimiter': {
						'thousands': ' ',
						'decimal':   ','
					}
				},
				'in':  1234567.25,
				'out': '1 234 567,250'
			},
		]

		for c in cases:

			options = c.get('options', None)

			if options is None:

				self.assertEqual(Clayful.format_number(c.get('in')), c.get('out'))

			else:
				self.assertEqual(Clayful.format_number(c.get('in'), options), c.get('out'))


	def test_format_price(self):

		cases = [
			{
				'in':  None,
				'out': ''
			},
			{
				'in':  0,
				'out': '0'
			},
			{
				'options': {},
				'in':      0,
				'out':     '0'
			},
			{
				'in':  1234567.25,
				'out': '1234567.25'
			},
			{
				'options': {},
				'in':      1234567.25,
				'out':     '1234567.25'
			},
			{
				'options': {
					'symbol':    '$',
					'format':    '{symbol}{price}',
					'precision': 2,
					'delimiter': {
						'thousands': ',',
						'decimal':   '.'
					}
				},
				'in':  1234567.25,
				'out': '$1,234,567.25'
			},
			{
				'options': {
					'symbol':    'won',
					'format':    '{price} {symbol}',
					'precision': 0,
					'delimiter': {
						'thousands': ',',
						'decimal':   '.'
					}
				},
				'in':  1234567.25,
				'out': '1,234,567 won'
			}
		]

		for c in cases:

			options = c.get('options', None)

			if options is None:

				self.assertEqual(Clayful.format_price(c.get('in')), c.get('out'))

			else:
				self.assertEqual(Clayful.format_price(c.get('in'), options), c.get('out'))