import pydantic
import requests
import unittest

from sys import stderr

from shop.api.common import ShopApiRouter, STATUS_CODE_OK
from shop.api.models.product import ModelProduct as product_model


# client = RequestsClient()
# client = RequestsClient()
# response = client.get('http://testserver/users/')
# assert response.status_code == 200


class TestShop(unittest.TestCase):
	"""
	Shop's API test case
	"""

	products: list[product_model]

	@staticmethod
	def _make_request(request, url, params=None) -> requests.Response:
		try:
			return request(url, params=params)
		except Exception as e:
			print('Request exception:\n\t', e, file=stderr)

	@staticmethod
	def _delete_product(product_id) -> requests.Response:
		response = TestShop._make_request(requests.get,
		                                  ShopApiRouter.DELETE_PRODUCT_URL,
		                                  {product_model.get_id_key(): product_id})
		if response.status_code != STATUS_CODE_OK:
			raise Exception(f'Failed to delete product with id "{product_id}"')
		return response

	@staticmethod
	def _get_products() -> list[product_model]:
		return TestShop._make_request(requests.get, ShopApiRouter.GET_ALL_PRODUCTS_URL).json()

	def __init__(self, *args, **kwargs):
		super(TestShop, self).__init__(*args, **kwargs)

		print('Starting shop''s Rest API tests')

		self.addCleanup(self._delete_existing_products)
		self.addCleanup(lambda: print('Deleting products after unit test is complete'))

	@classmethod
	def _delete_existing_products(cls) -> None:
		products = TestShop._get_products() if len(cls.products) == 0 else cls.products
		for i, product in enumerate(products):
			try:
				parsed_product = cls.product_model.parse_obj(product)
				print(f'Deleteing product with id "{parsed_product.id}"')
				TestShop._delete_product(parsed_product.id)
			except pydantic.ValidationError as e:
				print(f'Exception was thrown while deleting {i} product.\n' + e.json(), file=stderr)
			except Exception as e:
				print(e, file=stderr)

	@classmethod
	def test_get_all_products(cls):
		cls.assertEqual(1, 1)


if __name__ == '__main__':
	unittest.main()
