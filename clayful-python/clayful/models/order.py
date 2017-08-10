class Order:

	Clayful = None
	name = 'Order'
	path = 'orders'

	@staticmethod
	def config(clayful):

		Order.Clayful = clayful

		return Order

	@staticmethod
	def query(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/orders',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/orders',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/orders/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/orders/{orderId}',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def query_by_customer(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'query_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/orders',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def list_by_customer(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'list_by_customer',
			'http_method':      'GET',
			'path':             '/v1/customers/{customerId}/orders',
			'params':           ('customerId', ),
			'args':             args
		})

	@staticmethod
	def get_ticket_details(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'get_ticket_details',
			'http_method':      'GET',
			'path':             '/v1/orders/tickets/{code}/details',
			'params':           ('code', ),
			'args':             args
		})

	@staticmethod
	def get_sync_operation_errors(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'get_sync_operation_errors',
			'http_method':      'GET',
			'path':             '/v1/orders/{orderId}/sync/operations/errors',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def create_fulfillment(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_fulfillment',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/fulfillments',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def recover(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'recover',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/recover',
			'params':           ('orderId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def cancel(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'cancel',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/cancel',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def reject(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'reject',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/reject',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def undone(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'undone',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/undone',
			'params':           ('orderId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def done(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'done',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/done',
			'params':           ('orderId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def verify_ticket(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'verify_ticket',
			'http_method':      'POST',
			'path':             '/v1/orders/tickets/{code}/verify',
			'params':           ('code', ),
			'args':             args
		})

	@staticmethod
	def use_ticket(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'use_ticket',
			'http_method':      'POST',
			'path':             '/v1/orders/tickets/{code}/use',
			'params':           ('code', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def recover_ticket(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'recover_ticket',
			'http_method':      'POST',
			'path':             '/v1/orders/tickets/{code}/recover',
			'params':           ('code', ),
			'args':             args
		})

	@staticmethod
	def create_full_payment_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_full_payment_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/transactions/full',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def create_all_fulfillments(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_all_fulfillments',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/fulfillments/all',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def create_full_refund(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_full_refund',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/full',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def create_partial_payment_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_partial_payment_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/transactions/partial',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def create_partial_refund(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_partial_refund',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/partial',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def reject_refund(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'reject_refund',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/reject',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def sync_payment_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'sync_payment_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/transactions/{transactionId}/sync',
			'params':           ('orderId', 'transactionId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def increase_metafield(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'increase_metafield',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/meta/{field}/inc',
			'params':           ('orderId', 'field', ),
			'args':             args
		})

	@staticmethod
	def push_to_metafield(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'push_to_metafield',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/meta/{field}/push',
			'params':           ('orderId', 'field', ),
			'args':             args
		})

	@staticmethod
	def pull_from_metafield(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'pull_from_metafield',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/meta/{field}/pull',
			'params':           ('orderId', 'field', ),
			'args':             args
		})

	@staticmethod
	def recover_download(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'recover_download',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/items/{itemId}/download/recover',
			'params':           ('orderId', 'itemId', ),
			'args':             args
		})

	@staticmethod
	def partial_restock(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'partial_restock',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/restock/partial',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def create_full_refund_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_full_refund_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/transactions/full',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def full_restock(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'full_restock',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/restock/full',
			'params':           ('orderId', 'refundId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def create_downloadable_url(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_downloadable_url',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/items/{itemId}/download/url',
			'params':           ('orderId', 'itemId', ),
			'args':             args
		})

	@staticmethod
	def create_partial_refund_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'create_partial_refund_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/transactions/partial',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def sync_refund_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'sync_refund_transaction',
			'http_method':      'POST',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/transactions/{transactionId}/sync',
			'params':           ('orderId', 'refundId', 'transactionId', ),
			'without_payload':  True,
			'args':             args
		})

	@staticmethod
	def update(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def update_fulfillment(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update_fulfillment',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}/fulfillments/{fulfillmentId}',
			'params':           ('orderId', 'fulfillmentId', ),
			'args':             args
		})

	@staticmethod
	def update_item(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update_item',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}/items/{itemId}',
			'params':           ('orderId', 'itemId', ),
			'args':             args
		})

	@staticmethod
	def update_payment_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update_payment_transaction',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}/transactions/{transactionId}',
			'params':           ('orderId', 'transactionId', ),
			'args':             args
		})

	@staticmethod
	def update_refund(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update_refund',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def update_refund_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'update_refund_transaction',
			'http_method':      'PUT',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/transactions/{transactionId}',
			'params':           ('orderId', 'refundId', 'transactionId', ),
			'args':             args
		})

	@staticmethod
	def delete(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}',
			'params':           ('orderId', ),
			'args':             args
		})

	@staticmethod
	def delete_payment_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_payment_transaction',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/transactions/{transactionId}',
			'params':           ('orderId', 'transactionId', ),
			'args':             args
		})

	@staticmethod
	def delete_refund(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_refund',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}',
			'params':           ('orderId', 'refundId', ),
			'args':             args
		})

	@staticmethod
	def delete_fulfillment(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_fulfillment',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/fulfillments/{fulfillmentId}',
			'params':           ('orderId', 'fulfillmentId', ),
			'args':             args
		})

	@staticmethod
	def delete_metafield(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_metafield',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/meta/{field}',
			'params':           ('orderId', 'field', ),
			'args':             args
		})

	@staticmethod
	def delete_sync_operation(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_sync_operation',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/sync/operations/{operationId}',
			'params':           ('orderId', 'operationId', ),
			'args':             args
		})

	@staticmethod
	def delete_refund_transaction(*args):

		return Order.Clayful.call_api({
			'model_name':       Order.name,
			'method_name':      'delete_refund_transaction',
			'http_method':      'DELETE',
			'path':             '/v1/orders/{orderId}/refunds/{refundId}/transactions/{transactionId}',
			'params':           ('orderId', 'refundId', 'transactionId', ),
			'args':             args
		})

