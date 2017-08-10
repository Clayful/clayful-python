class Subscription:

	Clayful = None
	name = 'Subscription'
	path = ''

	@staticmethod
	def config(clayful):

		Subscription.Clayful = clayful

		return Subscription

	@staticmethod
	def query(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/subscriptions',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/subscriptions',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/subscriptions/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/subscriptions/{subscriptionId}',
			'params':           ('subscriptionId', ),
			'args':             args
		})

	@staticmethod
	def query_by_customer(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'query_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/subscriptions',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def list_by_customer(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'list_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/subscriptions',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def reject(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'reject',
			'http_method':      'POST',
			'path':             '/v1/subscriptions/{subscriptionId}/reject',
			'params':           ('subscriptionId', ),
			'args':             args
		})

	@staticmethod
	def cancel(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'cancel',
			'http_method':      'POST',
			'path':             '/v1/subscriptions/{subscriptionId}/cancel',
			'params':           ('subscriptionId', ),
			'args':             args
		})

	@staticmethod
	def start(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'start',
			'http_method':      'POST',
			'path':             '/v1/subscriptions/{subscriptionId}/start',
			'params':           ('subscriptionId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return Subscription.Clayful.call_api({
			'model_name':       Subscription.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/subscriptions/{subscriptionId}',
			'params':           ('subscriptionId', ),
			'args':             args
		})

