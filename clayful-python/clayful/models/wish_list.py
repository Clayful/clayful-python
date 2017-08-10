class WishList:

	Clayful = None
	name = 'WishList'
	path = 'wishlists'

	@staticmethod
	def config(clayful):

		WishList.Clayful = clayful

		return WishList

	@staticmethod
	def query(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def query_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'query_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'list_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/wishlists/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def query_by_customer(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'query_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/wishlists',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def list_by_customer(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'list_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/wishlists',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def count_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'count_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'get_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def query_products(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'query_products',
			'http_method':      'GET',
			'path':             '/v1/wishlists/{wishListId}/products',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def list_products(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'list_products',
			'http_method':      'GET',
			'path':             '/v1/wishlists/{wishListId}/products',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def query_products_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'query_products_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists/{wishListId}/products',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def list_products_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'list_products_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists/{wishListId}/products',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def count_products(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'count_products',
			'http_method':      'GET',
			'path':             '/v1/wishlists/{wishListId}/products/count',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def count_products_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'count_products_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/wishlists/{wishListId}/products/count',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def create(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'create',
			'http_method':      'POST',
			'path':             '/v1/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def create_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'create_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/wishlists',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def add_item(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'add_item',
			'http_method':      'POST',
			'path':             '/v1/wishlists/{wishListId}/items',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def add_item_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'add_item_as_me',
			'http_method':      'POST',
			'path':             '/v1/me/wishlists/{wishListId}/items',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def increase_metafield(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'increase_metafield',
			'http_method':      'POST',
			'path':             '/v1/wishlists/{wishListId}/meta/{field}/inc',
			'params':           ('wishListId', 'field', ),
			'args':             args
		})

	@staticmethod
	def push_to_metafield(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'push_to_metafield',
			'http_method':      'POST',
			'path':             '/v1/wishlists/{wishListId}/meta/{field}/push',
			'params':           ('wishListId', 'field', ),
			'args':             args
		})

	@staticmethod
	def pull_from_metafield(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'pull_from_metafield',
			'http_method':      'POST',
			'path':             '/v1/wishlists/{wishListId}/meta/{field}/pull',
			'params':           ('wishListId', 'field', ),
			'args':             args
		})

	@staticmethod
	def update(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'update',
			'http_method':      'PUT',
			'path':             '/v1/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def update_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'update_as_me',
			'http_method':      'PUT',
			'path':             '/v1/me/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def delete_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'delete_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/wishlists/{wishListId}',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def empty(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'empty',
			'http_method':      'DELETE',
			'path':             '/v1/wishlists/{wishListId}/items',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def empty_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'empty_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/wishlists/{wishListId}/items',
			'params':           ('wishListId', ),
			'args':             args
		})

	@staticmethod
	def delete_item(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'delete_item',
			'http_method':      'DELETE',
			'path':             '/v1/wishlists/{wishListId}/items/{productId}',
			'params':           ('wishListId', 'productId', ),
			'args':             args
		})

	@staticmethod
	def delete_metafield(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'delete_metafield',
			'http_method':      'DELETE',
			'path':             '/v1/wishlists/{wishListId}/meta/{field}',
			'params':           ('wishListId', 'field', ),
			'args':             args
		})

	@staticmethod
	def delete_item_as_me(*args):

		return WishList.Clayful.call_api({
			'model_name':       WishList.name,
			'method_name':      'delete_item_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/wishlists/{wishListId}/items/{productId}',
			'params':           ('wishListId', 'productId', ),
			'args':             args
		})

