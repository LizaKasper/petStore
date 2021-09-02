import unittest
import requests

class TestStringMethods(unittest.TestCase):

	def test_store_inventory(self):
		r = requests.get('https://petstore.swagger.io/v2/store/inventory', params={'id': '1', 'petId': '3','quantity': '4'})
		assert r.status_code == 200

	def test_store_order(self):
		payload = {'id': '1', 'petId': '3','quantity': '4'}
		r = requests.put('https://petstore.swagger.io/v2/store/order', data = {'id': '1'})
		assert r.status_code == 200


	def test_store_order_orderid(self):
		r = requests.get('https://petstore.swagger.io/v2/store/order/1')
		assert r.status_code == 200

	def test_store_delete(self):
		r = requests.delete('https://petstore.swagger.io/v2/store/order/1')
		assert r.status_code == 200


if __name__ == '__main__':
    unittest.main()