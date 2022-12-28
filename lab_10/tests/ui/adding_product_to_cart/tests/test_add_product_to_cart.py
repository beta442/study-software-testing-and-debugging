from typing import Union
from unittest import TestCase


from tests.ui.adding_product_to_cart.web_driver_methods.ProductCartMethods import\
	ProductCartMethods as WebDriverMethods

from shop.ShopRouter import ShopRouter


class TestCaseAddProductToCart(TestCase):
	__BASE_URL = ShopRouter.BASE_URL

	def setUp(self) -> None:
		self.__webdriver_methods = WebDriverMethods()

		self.__webdriver_methods.get(self.__BASE_URL)

	def test_cart_is_empty_on_init(self):
		is_cart_empty = self.__webdriver_methods.is_cart_empty()

		self.assertTrue(is_cart_empty,
		                f"""
		                Expected to see empty cart on DOM load at {self.__BASE_URL}
		                """)

	def test_add_all_products_on_page_to_cart(self):
		self.__webdriver_methods.add_all_products_on_current_page()
		expected_cart_costs = self.__webdriver_methods.get_expected_product_costs()
		expected_ids = self.__webdriver_methods.get_expected_product_ids_in_cart()
		expected_titles = self.__webdriver_methods.get_product_titles_on_current_page()

		actual_cart_costs = self.__webdriver_methods.get_actual_product_costs_in_cart()
		actual_ids = self.__webdriver_methods.get_actual_product_ids_in_cart()
		actual_titles = self.__webdriver_methods.get_actual_product_titles_in_cart()

		self.assertEqual(expected_ids,
		                 actual_ids,
		                 f"""
		                 Expected to get same ids from cart as was on shopping page at {self.__BASE_URL}
		                 Expected: {expected_ids}
		                 Got: {actual_ids}
		                 """)
		self.assertEqual(sum(expected_cart_costs),
		                 sum(actual_cart_costs),
		                 f"""
		                 Expected to get same cart cost as was total products cost on shopping page at {self.__BASE_URL}
		                 Expected: {sum(expected_cart_costs)}
		                 Got: {sum(actual_cart_costs)}
		                 """)
		self.assertEqual([x.lower() for x in expected_titles],
		                 [x.lower() for x in actual_titles],
		                 f"""
		                 Expected to get actual product titles in cart after adding them on shopping page at {self.__BASE_URL}
		                 Excpected: {expected_titles}
		                 Go: {actual_titles}
		                 """)

	def test_add_single_product(self):
		self.__webdriver_methods.go_to_single_product_page()
		expected_product_title = self.__webdriver_methods.get_single_product_title()
		expected_product_price = self.__webdriver_methods.get_single_product_price()
		expected_product_id = self.__webdriver_methods.get_single_product_id()
		expected_quantity_input_field = 100
		self.__webdriver_methods.set_single_product_quantity(expected_quantity_input_field)

		self.__webdriver_methods.press_add_single_product()

		actual_product_ids_in_cart = self.__webdriver_methods.get_actual_product_ids_in_cart()
		actual_product_titles_in_cart = self.__webdriver_methods.get_actual_product_titles_in_cart()
		actual_product_costs_int_cart = self.__webdriver_methods.get_actual_product_costs_in_cart()

		self.assertIn(expected_product_title.lower(),
		              [title.lower() for title in actual_product_titles_in_cart],
		              f"""
		              Expected to find single product's title in cart
		              Expected title: {expected_product_title.lower()}
		              Got: {actual_product_titles_in_cart}
		              """)
		self.assertIn(expected_product_id,
		              actual_product_ids_in_cart,
		              f"""
		              Expected to find single product's id in cart
		              Expected id: {expected_product_id}
		              Got: {actual_product_ids_in_cart} 
		              """)
		self.assertIn(expected_product_price,
		              actual_product_costs_int_cart,
		              f"""
		              Expected to find single product's cost in cart
		              Expected price: {expected_product_price}
		              Got: {actual_product_costs_int_cart}
		              """)


__all__ = [
	'TestCaseAddProductToCart'
]
