import unittest

from parameterized import parameterized

from rest_api.shop.common import \
	PK_ID, \
	PK_TITLE, \
 \
	RK_STATUS
from rest_api.shop.model.product import PRODUCT_ALIAS_POSTFIX
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
		print(f'Start {cls.__name__}\n')

	@classmethod
	def tearDownClass(cls) -> None:
		print('\nClassCleanUp: deleting all created  products')
		cls._delete_existing_products(cls)

	def setUp(self) -> None:
		print(f'Start {self._testMethodName}')

	def _delete_existing_products(self) -> None:
		for item in self.__products_ids:
			print(f'Deleting product with id "{item}"')
			response = ShopApi.delete_product(item)
			if response.status != self.VALID_STATUS:
				print(f'Failed to delete product with {item}. Status is {response.status}')
		self.__products_ids.clear()

	@parameterized.expand([
		TC_ADD_PRODUCT_VALID_ALMOST_EMPTY_SCHEMA_KEY,
		TC_ADD_PRODUCT_VALID_KEY,
		TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID_KEY,
		TC_ADD_PRODUCT_VALID_WITHOUT_ID_KEY
	])
	def test_add_valid_products(self, test_key):
		product = TC_ADD_PRODUCT_VALID_JSON[test_key]
		response = ShopApi.add_product(product).dict()
		self.__products_ids.append(response[PK_ID])
		print(f'Added product with {response[PK_ID]} id')

		self.assertEqual(response[RK_STATUS],
		                 self.VALID_STATUS,
		                 f"""
						 Test case for: {test_key} product\n
						 Expected {self.VALID_STATUS} value at repsonse's {RK_STATUS} member while adding product\n
						 """)

	@parameterized.expand([
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 0),
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 1),
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 2),
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 3),

		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '' + PRODUCT_ALIAS_POSTFIX * 0),
		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '0' + PRODUCT_ALIAS_POSTFIX * 1),
		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '0' + PRODUCT_ALIAS_POSTFIX * 2),
		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '0' + PRODUCT_ALIAS_POSTFIX * 3),
	])
	def test_alias_product(self, test_key, expected_postfix):
		product = TC_ADD_PRODUCT_VALID_ALIAS_JSON[test_key]
		response = ShopApi.add_product(product).dict()
		self.__products_ids.append(response[PK_ID])
		print(f'Added product with {response[PK_ID]} id')
		added_product = ShopApi.get_product(response[PK_ID])

		self.assertEqual(response[RK_STATUS],
		                 self.VALID_STATUS,
		                 f"""
						 Test case for: {test_key} product\n
						 Expected {self.VALID_STATUS} value at repsonse's {RK_STATUS} member while testing product''s alias\n
						 """)
		self.assertIsNot(added_product,
		                 None,
		                 f"""
		                 Test case for: {test_key} product\n
		                 Expected get product from db while testing product aliases
						 """)
		self.assertEqual(product[PK_TITLE].lower() + expected_postfix,
		                 added_product.alias,
		                 f"""
		                 Test case for: {test_key} product\n
		                 Expected '{expected_postfix}' postfix in added_product alias\n
		                 Got '{added_product.alias}'
					     """)


if __name__ == '__main__':
	unittest.main()
