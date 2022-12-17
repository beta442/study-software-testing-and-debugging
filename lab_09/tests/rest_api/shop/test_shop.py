import unittest

from parameterized import parameterized

from rest_api.shop.common import PK_ID, RK_STATUS
from rest_api.shop.shop_api import ShopApi

from tests.rest_api.shop.test_cases_json.loader import *


class ShopRestApiTest(unittest.TestCase):
	"""
	Shop''s rest API tests
	"""

	INVALID_STATUS: int = 0
	VALID_STATUS: int = 1

	__products_ids: list[int] = list()

	@classmethod
	def setUpClass(cls) -> None:
		print(f'Start {cls.__name__}')

		cls.addClassCleanup(lambda: cls._delete_existing_products(cls))
		cls.addClassCleanup(lambda: print('ClassCleanUp: deleting all created  products'))

	def setUp(self) -> None:
		print(f'Start {self._testMethodName}')

	def _delete_existing_products(self) -> None:
		for item in self.__products_ids:
			print(f'Deleteing product with id "{item}"')
			response = ShopApi.delete_product(item)
			if response.status != self.VALID_STATUS:
				print(f'Failed to delete product with {item}. Status is {response.status}')
		self.__products_ids.clear()

	@parameterized.expand([
		TC_ADD_PRODUCT_VALID_KEY,
		TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID,
		TC_ADD_PRODUCT_VALID_WITHOUT_ID
	])
	def test_add_valid_products(self, test_key):
		product = TC_ADD_PRODUCT_JSON[test_key]
		response = ShopApi.add_product(product).dict()
		print(f'Added product with {response[PK_ID]} id')

		self.assertEqual(response[RK_STATUS],
		                 self.VALID_STATUS,
		                 f"""
						 Test case for: {test_key} product\n
						 Expected {self.VALID_STATUS} value at repsonse's {RK_STATUS} member\n
						 """)
		self.__products_ids.append(response[PK_ID])


if __name__ == '__main__':
	unittest.main()
