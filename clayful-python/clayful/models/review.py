class Review:

	Clayful = None
	name = 'Review'
	path = 'products/reviews'

	@staticmethod
	def config(clayful):

		Review.Clayful = clayful

		return Review

	@staticmethod
	def query(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/products/reviews',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/products/reviews',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/products/reviews/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/products/reviews/{reviewId}',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def query_by_product(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'query_by_product',
			'http_method':      'GET',
			'path':             '/v1/products/{productId}/reviews',
			'params':           ('productId', ),
			'args':             args
		})

	@staticmethod
	def list_by_product(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'list_by_product',
			'http_method':      'GET',
			'path':             '/v1/products/{productId}/reviews',
			'params':           ('productId', ),
			'args':             args
		})

	@staticmethod
	def query_by_customer(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'query_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/products/reviews',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def list_by_customer(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'list_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/products/reviews',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def create(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'create',
			'http_method':      'POST',
			'path':             '/v1/products/reviews',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def create_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'create_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def flag(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'flag',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/flag',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def flag_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'flag_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews/{reviewId}/flag',
			'params':           ('reviewId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def helped(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'helped',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/helped/{upDown}',
			'params':           ('reviewId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def cancel_flag(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'cancel_flag',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/flag/cancel',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def cancel_flag_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'cancel_flag_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews/{reviewId}/flag/cancel',
			'params':           ('reviewId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def helped_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'helped_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews/{reviewId}/helped/{upDown}',
			'params':           ('reviewId', 'upDown', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def push_to_metafield(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'push_to_metafield',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/meta/{field}/push',
			'params':           ('reviewId', 'field', ),
			'args':             args
		})

	@staticmethod
	def pull_from_metafield(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'pull_from_metafield',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/meta/{field}/pull',
			'params':           ('reviewId', 'field', ),
			'args':             args
		})

	@staticmethod
	def cancel_helped(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'cancel_helped',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/helped/{upDown}/cancel',
			'params':           ('reviewId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def increase_metafield(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'increase_metafield',
			'http_method':      'POST',
			'path':             '/v1/products/reviews/{reviewId}/meta/{field}/inc',
			'params':           ('reviewId', 'field', ),
			'args':             args
		})

	@staticmethod
	def cancel_helped_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'cancel_helped_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews/{reviewId}/helped/{upDown}/cancel',
			'params':           ('reviewId', 'upDown', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def update(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'update',
			'http_method':      'PUT',
			'path':             '/v1/products/reviews/{reviewId}',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def update_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'update_as_me',
			'http_method':      'PUT',
			'path':             '/v1/me/products/reviews/{reviewId}',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def update_as_customer(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'update_as_customer',
			'http_method':      'PUT',
			'path':             '/v1/customers/{customerId}/products/reviews/{reviewId}',
			'params':           ('customerId', 'reviewId', ),
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/products/reviews/{reviewId}',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def delete_as_me(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'delete_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/products/reviews/{reviewId}',
			'params':           ('reviewId', ),
			'args':             args
		})

	@staticmethod
	def delete_metafield(*args):

		return Review.Clayful.call_api({
			'model_name':       Review.name,
			'method_name':      'delete_metafield',
			'http_method':      'DELETE',
			'path':             '/v1/products/reviews/{reviewId}/meta/{field}',
			'params':           ('reviewId', 'field', ),
			'args':             args
		})

