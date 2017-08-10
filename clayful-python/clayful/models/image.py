class Image:

	Clayful = None
	name = 'Image'
	path = 'images'

	@staticmethod
	def config(clayful):

		Image.Clayful = clayful

		return Image

	@staticmethod
	def query(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/images',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/images',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/images/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/images/{imageId}',
			'params':           ('imageId', ),
			'args':             args
		})

	@staticmethod
	def create(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'create',
			'http_method':      'POST',
			'path':             '/v1/images',
			'params':           (),
			'uses_form_data':   True,
			'args':             args
		})

	@staticmethod
	def add_to_review_as_me(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'add_to_review_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/products/reviews/{reviewId}/images',
			'params':           ('reviewId', ),
			'uses_form_data':   True,
			'args':             args
		})

	@staticmethod
	def update(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'update',
			'http_method':      'PUT',
			'path':             '/v1/images/{imageId}',
			'params':           ('imageId', ),
			'uses_form_data':   True,
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/images/{imageId}',
			'params':           ('imageId', ),
			'args':             args
		})

	@staticmethod
	def delete_from_review_as_me(*args):

		return Image.Clayful.call_api({
			'model_name':       Image.name,
			'method_name':      'delete_from_review_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/products/reviews/{reviewId}/images/{imageId}',
			'params':           ('reviewId', 'imageId', ),
			'args':             args
		})

