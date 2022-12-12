import pydantic
import unittest

from sys import stderr

from shop.api.models.product import ModelProduct as product_model
from shop.api.shop_api import ShopApi


class TestShop(unittest.TestCase):
	"""
	Shop's API test case
	"""

	def __init__(self, *args, **kwargs):
		super(TestShop, self).__init__(*args, **kwargs)

		self.__products: list[product_model] = list()

		print('Starting shop''s Rest API tests')

		self.addCleanup(self._delete_existing_products)
		self.addCleanup(lambda: print('Deleting products after unit test is complete'))

	def _delete_existing_products(self) -> None:
		products = ShopApi.get_products() if len(self.__products) == 0 else self.__products
		for i, product in enumerate(products):
			try:
				parsed_product = product_model.parse_obj(product)
				print(f'Deleteing product with id "{parsed_product.id}"')
				ShopApi.delete_product(parsed_product.id)
			except pydantic.ValidationError as e:
				print(f'Exception was thrown while deleting {i} product.\n' + e.json(), file=stderr)
			except Exception as e:
				print(e, file=stderr)

	@classmethod
	def test_get_all_products(cls):
		cls.assertTrue(True)


if __name__ == '__main__':
	unittest.main()
