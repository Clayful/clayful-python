class Customer:

	Clayful = None
	name = 'Customer'
	path = 'customers'

	@staticmethod
	def config(clayful):

		Customer.Clayful = clayful

		return Customer

	@staticmethod
	def query(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/customers',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/customers',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'get_me',
			'http_method':      'GET',
			'path':             '/v1/me',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/customers/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def query_coupons_as_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_coupons_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/coupons',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list_coupons_as_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_coupons_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/coupons',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def query_coupons(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_coupons',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/coupons',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def list_coupons(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_coupons',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/coupons',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def query_by_group(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_by_group',
			'http_method':      'GET',
			'path':             '/v1/groups/{groupId}/customers',
			'params':           ('groupId', ),
			'args':             args
		})

	@staticmethod
	def list_by_group(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_by_group',
			'http_method':      'GET',
			'path':             '/v1/groups/{groupId}/customers',
			'params':           ('groupId', ),
			'args':             args
		})

	@staticmethod
	def count_coupons_as_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'count_coupons_as_me',
			'http_method':      'GET',
			'path':             '/v1/me/coupons/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count_coupons(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'count_coupons',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/coupons/count',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def query_by_flag_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_by_flag_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/flagged/customers',
			'params':           ('voteModel', 'voteModelId', ),
			'args':             args
		})

	@staticmethod
	def list_by_flag_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_by_flag_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/flagged/customers',
			'params':           ('voteModel', 'voteModelId', ),
			'args':             args
		})

	@staticmethod
	def query_by_flag_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_by_flag_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/flagged/customers',
			'params':           ('voteModel', 'voteModelId', ),
			'args':             args
		})

	@staticmethod
	def list_by_flag_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_by_flag_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/flagged/customers',
			'params':           ('voteModel', 'voteModelId', ),
			'args':             args
		})

	@staticmethod
	def query_by_help_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_by_help_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/helped/{upDown}/customers',
			'params':           ('voteModel', 'voteModelId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def list_by_help_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_by_help_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/helped/{upDown}/customers',
			'params':           ('voteModel', 'voteModelId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def query_by_help_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'query_by_help_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/helped/{upDown}/customers',
			'params':           ('voteModel', 'voteModelId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def list_by_help_votes(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'list_by_help_votes',
			'http_method':      'GET',
			'path':             '/v1/{voteModel}/{voteModelId}/helped/{upDown}/customers',
			'params':           ('voteModel', 'voteModelId', 'upDown', ),
			'args':             args
		})

	@staticmethod
	def create(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'create',
			'http_method':      'POST',
			'path':             '/v1/customers',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def signup(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'signup',
			'http_method':      'POST',
			'path':             '/v1/me',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def auth(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'auth',
			'http_method':      'POST',
			'path':             '/v1/customers/auth',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def create_verification(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'create_verification',
			'http_method':      'POST',
			'path':             '/v1/customers/verifications',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def add_coupon_to_customers(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'add_coupon_to_customers',
			'http_method':      'POST',
			'path':             '/v1/coupons/{couponId}/customers',
			'params':           ('couponId', ),
			'args':             args
		})

	@staticmethod
	def request_verification_email(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'request_verification_email',
			'http_method':      'POST',
			'path':             '/v1/customers/verifications/emails',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def verify(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'verify',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/verify',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def add_coupon(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'add_coupon',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/coupons',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def reset_password(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'reset_password',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/password/reset',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def increase_metafield(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'increase_metafield',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/meta/{field}/inc',
			'params':           ('customerId', 'field', ),
			'args':             args
		})

	@staticmethod
	def push_to_metafield(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'push_to_metafield',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/meta/{field}/push',
			'params':           ('customerId', 'field', ),
			'args':             args
		})

	@staticmethod
	def pull_from_metafield(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'pull_from_metafield',
			'http_method':      'POST',
			'path':             '/v1/customers/{customerId}/meta/{field}/pull',
			'params':           ('customerId', 'field', ),
			'args':             args
		})

	@staticmethod
	def update_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'update_me',
			'http_method':      'PUT',
			'path':             '/v1/me',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def update(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'update',
			'http_method':      'PUT',
			'path':             '/v1/customers/{customerId}',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def update_credentials_as_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'update_credentials_as_me',
			'http_method':      'PUT',
			'path':             '/v1/me/credentials',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def update_credentials(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'update_credentials',
			'http_method':      'PUT',
			'path':             '/v1/customers/{customerId}/credentials',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def delete_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'delete_me',
			'http_method':      'DELETE',
			'path':             '/v1/me',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/customers/{customerId}',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def delete_coupon_as_me(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'delete_coupon_as_me',
			'http_method':      'DELETE',
			'path':             '/v1/me/coupons/{couponId}',
			'params':           ('couponId', ),
			'args':             args
		})

	@staticmethod
	def delete_metafield(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'delete_metafield',
			'http_method':      'DELETE',
			'path':             '/v1/customers/{customerId}/meta/{field}',
			'params':           ('customerId', 'field', ),
			'args':             args
		})

	@staticmethod
	def delete_coupon(*args):

		return Customer.Clayful.call_api({
			'model_name':       Customer.name,
			'method_name':      'delete_coupon',
			'http_method':      'DELETE',
			'path':             '/v1/customers/{customerId}/coupons/{couponId}',
			'params':           ('customerId', 'couponId', ),
			'args':             args
		})

