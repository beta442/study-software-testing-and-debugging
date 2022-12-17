import unittest

from parameterized import parameterized

from rest_api.shop.body.edit_product import ModelEditProductBody
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

	_products_ids: list[int] = list()
	_PRODUCT_COUNT_BEFORE: int = 0

	@classmethod
	def setUpClass(cls) -> None:
		print(f'Start {cls.__name__}\n')
		cls._PRODUCT_COUNT_BEFORE = ShopApi.get_product_count()

	@classmethod
	def tearDownClass(cls) -> None:
		total_count_product = ShopApi.get_product_count()
		expected_count_product = cls._PRODUCT_COUNT_BEFORE + len(cls._products_ids)
		cls.assertTrue(cls,
		               expected_count_product == total_count_product,
		               f"""
		               Not all products have been added
		               Expected that {total_count_product} products would be added
		               """)

		print('\nClassCleanUp: deleting all created products')
		cls._delete_existing_products(cls)

	def setUp(self) -> None:
		print(f'\nStart {self._testMethodName}')

	def _delete_existing_products(self) -> None:
		for item in self._products_ids:
			print(f'Deleting product with id "{item}"')
			response = ShopApi.delete_product(item)
			if response.status != self.VALID_STATUS:
				raise RuntimeError(f'Failed to delete product with {item} id. Status is {response.status}')
		self._products_ids.clear()

	@parameterized.expand([
		TC_ADD_PRODUCT_VALID_ALMOST_EMPTY_SCHEMA_KEY,
		TC_ADD_PRODUCT_VALID_KEY,
		TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID_KEY,
		TC_ADD_PRODUCT_VALID_WITHOUT_ID_KEY
	])
	def test_add_valid_products(self, test_key):
		product = TC_ADD_PRODUCT_VALID_JSON[test_key]
		response = ShopApi.add_product(product).dict()
		self._products_ids.append(response[PK_ID])
		print(f'Add product with {response[PK_ID]} id')

		self.assertEqual(response[RK_STATUS],
		                 self.VALID_STATUS,
		                 f"""
						 Test case for: {test_key} product\n
						 Expected {self.VALID_STATUS} value at response's {RK_STATUS} member while adding product\n
						 """)

	@parameterized.expand([
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 0),
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 1),
		(TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY, PRODUCT_ALIAS_POSTFIX * 2),

		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '' + PRODUCT_ALIAS_POSTFIX * 0),
		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '0' + PRODUCT_ALIAS_POSTFIX * 1),
		(TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY, '0' + PRODUCT_ALIAS_POSTFIX * 2),
	])
	def test_alias_product(self, test_key, expected_postfix):
		product = TC_ADD_PRODUCT_VALID_ALIAS_JSON[test_key]
		response = ShopApi.add_product(product).dict()
		self._products_ids.append(response[PK_ID])
		print(f'Add product with {response[PK_ID]} id')
		added_product = ShopApi.get_product(response[PK_ID])

		self.assertEqual(response[RK_STATUS],
		                 self.VALID_STATUS,
		                 f"""
						 Test case for: {test_key} product\n
						 Expected {self.VALID_STATUS} value at response's {RK_STATUS} member while testing product''s alias\n
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
		                 Expected '{product[PK_TITLE].lower() + expected_postfix}' alias in added_product\n
		                 Got '{added_product.alias}'
					     """)

	def test_delete_not_existing_product(self):
		not_valid_product_id = 0
		response = ShopApi.delete_product(not_valid_product_id)

		self.assertEqual(response.status,
		                 self.INVALID_STATUS,
		                 f"""
		                 Expected {self.INVALID_STATUS} status in response while deleting product with {not_valid_product_id} id
		                 """)

	def test_delete_product(self):
		product_id = self._products_ids.pop()
		response = ShopApi.delete_product(product_id)
		print(f'Delete product with {product_id} id')

		self.assertEqual(response.status,
		                 self.VALID_STATUS,
		                 f"""
		                 Expected {self.VALID_STATUS} status in response while deleting existing product with {product_id} id
						 """)

	@parameterized.expand([
		(TC_EDIT_PRODUCT_SMALLEST_EDIT_KEY),
		(TC_EDIT_PRODUCT_FULL_EDIT_KEY),
	])
	def test_edit_product(self, test_key):
		new_product = ModelEditProductBody.parse_obj(TC_EDIT_PRODUCT_JSON[test_key]).dict()
		response = ShopApi.edit_product(new_product)
		print(f'Edited product with {new_product[PK_ID]} id')
		actual_product = ShopApi.get_product(new_product[PK_ID]).dict()

		self.assertEqual(response.status,
		                 self.VALID_STATUS,
		                 f"""
		                 Expected {self.VALID_STATUS} status in response while editing existing product with {new_product[PK_ID]} id
						 """)
		# Check are keys updated
		for key in new_product.keys():
			if new_product[key] is None:
				continue
			self.assertEqual(actual_product[key],
			                 new_product[key],
			                 f"""
			                 While editing products
			                 Expected new value {new_product[key]} at key "{key}" in actual product.\n
			                 Got {actual_product[key]}
							 """)

	def test_edit_not_existing_product(self):
		product = TC_EDIT_PRODUCT_JSON[TC_EDIT_PRODUCT_NOT_EXISTING_KEY]
		response = ShopApi.edit_product(product)

		self.assertEqual(response.status,
		                 self.INVALID_STATUS,
		                 f"""
		                 Expected {self.INVALID_STATUS} status in response while editing not existing product
						 """)


if __name__ == '__main__':
	unittest.main()
