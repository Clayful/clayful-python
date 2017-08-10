class Warehouse:

	Clayful = None
	name = 'Warehouse'
	path = 'warehouses'

	@staticmethod
	def config(clayful):

		Warehouse.Clayful = clayful

		return Warehouse

	@staticmethod
	def query(*args):

		return Warehouse.Clayful.call_api({
			'model_name':       Warehouse.name,
			'method_name':      'query',
			'http_method':      'GET',
			'path':             '/v1/warehouses',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def list(*args):

		return Warehouse.Clayful.call_api({
			'model_name':       Warehouse.name,
			'method_name':      'list',
			'http_method':      'GET',
			'path':             '/v1/warehouses',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def count(*args):

		return Warehouse.Clayful.call_api({
			'model_name':       Warehouse.name,
			'method_name':      'count',
			'http_method':      'GET',
			'path':             '/v1/warehouses/count',
			'params':           (),
			'args':             args
		})

	@staticmethod
	def get(*args):

		return Warehouse.Clayful.call_api({
			'model_name':       Warehouse.name,
			'method_name':      'get',
			'http_method':      'GET',
			'path':             '/v1/warehouses/{warehouseId}',
			'params':           ('warehouseId', ),
			'args':             args
		})

