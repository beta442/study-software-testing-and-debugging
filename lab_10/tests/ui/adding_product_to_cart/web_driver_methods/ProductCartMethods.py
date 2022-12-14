from typing import Union

from tests.ui.BaseWebDriverMethods import BaseWebDriverMethods

from tests.ui.common import BOOL_MAKE_WEBDRIVER_HEADLESS, WEB_DRIVER_ARG_HEADLESS
from tests.webdriver.WebDriver import By, ChromeOptions, WebElement

from tests.ui.x_paths import *

from tests.ui.adding_product_to_cart.configs.loader import *


class ProductCartMethods(BaseWebDriverMethods):
	"""
	WebDriver's methods for shop's auth UI tests
	"""

	__product_ids: list[int] = list()
	__cart_product_cost: list[float] = list()
	__product_titles: list[str] = list()

	def __init__(self):
		options = None
		if BOOL_MAKE_WEBDRIVER_HEADLESS:
			options = ChromeOptions()
			options.add_argument(WEB_DRIVER_ARG_HEADLESS)

		super(ProductCartMethods, self).__init__(options=options)

		self._driver.implicitly_wait(3)

	def close_product_cart(self) -> None:
		while self._driver.find_element(By.XPATH, R_XPATH_CART_CLOSE_BTN).is_displayed():
			try:
				self._driver.find_element(By.XPATH, R_XPATH_CART_CLOSE_BTN).click()
			except Exception:
				pass

	def show_product_cart(self) -> None:
		try:
			cart_show_btn = self._driver.find_element(By.XPATH, R_XPATH_CART_SHOW_BTN)
			cart_show_btn.click()
		except Exception:
			pass

	def is_cart_empty(self) -> bool:
		self.show_product_cart()

		clear_btn = self._driver.find_element(By.XPATH, R_XPATH_CART_CLEAR_BTN)

		return not clear_btn.is_displayed()

	def add_all_products_on_current_page(self, count_products_cost=True, count_products=True) -> None:
		try:
			add_to_cart_btns = self._driver.find_elements(By.XPATH, R_XPATH_ADD_TO_CART)
			if count_products_cost:
				self.__cart_product_cost = self._count_total_price_on_page()
			if count_products:
				self.__product_titles = self._get_product_titles_on_current_page()
				self.__product_ids = self._get_product_ids_on_current_page()

			for btn in add_to_cart_btns:
				btn.click()
				# To unfocus cart
				self.close_product_cart()

		except Exception as e:
			print(f"""
				  Failed web method: {__name__}
				  Exception: {e}
				  """)

	def get_product_titles_on_current_page(self) -> list[str]:
		return self.__product_titles

	def get_actual_cart_cost(self) -> int:
		try:
			price = self._driver.find_element(By.XPATH, R_XPATH_CART_TOTAL_PRICE)

			return int(''.join(x for x in price.text if x.isdigit()))
		except Exception:
			return -1

	__TABLE_D_PRODUCT_TITLE_INDEX = 1
	__TABLE_D_PRODUCT_QUANTITY_INDEX = 2
	__TABLE_D_PRODUCT_COST_INDEX = 3

	__TRIES_UNTIL_CART_LOAD = 50

	def get_actual_product_costs_in_cart(self) -> list[float]:
		try:
			result: list[float] = []

			products = self._get_product_table_rows()

			# print(f'Found {len(products)} at try: {tries}')

			for idx, product in enumerate(products):
				table_ds = product.find_elements(By.TAG_NAME, 'td')

				# for _idx, d in enumerate(table_ds):
				# 	print(f'{_idx}: {d.text}')

				product_cost = float(table_ds[self.__TABLE_D_PRODUCT_COST_INDEX].text)
				result.append(product_cost)
				# print(f'Add {product_cost} of {idx}')

			return result
		except Exception as e:
			print(f"""
				  Failed web method: {__name__}
				  Exception: {e}
				  """)
			return []

	def get_actual_product_titles_in_cart(self) -> list[str]:
		try:
			result: list[str] = []

			products = self._get_product_table_rows()

			for idx, product in enumerate(products):
				table_ds = product.find_elements(By.TAG_NAME, 'td')

				title = table_ds[self.__TABLE_D_PRODUCT_TITLE_INDEX].text
				result.append(title)

			return result
		except Exception as e:
			print(f"""
				  Failed web method: {__name__}
				  Exception: {e}
				  """)
			return []

	def get_actual_product_ids_in_cart(self) -> list[int]:
		try:
			# TODO: retrieve from cart only when cart is loaded
			products_delete_btns = self._driver.find_elements(By.XPATH, R_XPATH_CART_PRODUCT_DELETE_SPAN)

			result: list[int] = list()
			for btn in products_delete_btns:
				price = int(btn.get_attribute('data-id'))
				result.append(price)

			return result
		except Exception:
			return []

	def go_to_single_product_page(self) -> None:
		try:
			self._driver.get(TC_CART_TEST_JSON[TC_ADD_SINGLE_PRODUCT][F_URL_KEY])
		except:
			pass

	def get_single_product_title(self) -> str:
		try:
			title = self._driver.find_element(By.XPATH, R_XPATH_SHELF_ITEM_PRODUCT_TITLE)

			return title.text
		except:
			return ''

	def get_single_product_price(self) -> float:
		try:
			price_str = self._driver.find_element(By.XPATH, R_XPATH_SHELF_ITEM_PRODUCT_PRICE).text

			clear_price_str = str()
			for c in price_str:
				if c.isdigit() or c in [',', '.']:
					clear_price_str += c

			return float(clear_price_str)
		except:
			return float()

	def get_single_product_id(self) -> int:
		try:
			add_product_to_cart_btn = self._driver.find_element(By.XPATH, R_XPATH_SHELF_ITEM_PRODUCT_ADD_TO_CART_BTN)
			product_id = add_product_to_cart_btn.get_attribute('data-id')

			return int(product_id)
		except:
			return int()

	def set_single_product_quantity(self, quantity: int) -> None:
		try:
			input_quantity = self._driver.find_element(By.XPATH, R_XPATH_SHELF_ITEM_PRODUCT_QUANTITY_TO_ORDER)

			input_quantity.clear()
			input_quantity.send_keys(quantity)
		except:
			pass

	def press_add_single_product(self) -> None:
		try:
			self.__product_ids.append(self.get_single_product_id())
			self.__product_titles.append(self.get_single_product_title())
			self.__cart_product_cost.append(self.get_single_product_price())

			add_btn = self._driver.find_element(By.XPATH, R_XPATH_SHELF_ITEM_PRODUCT_ADD_TO_CART_BTN)
			add_btn.click()

		except:
			pass

	def get_expected_product_ids_in_cart(self) -> list[int]:
		return self.__product_ids

	def get_expected_product_costs(self) -> list[float]:
		return self.__cart_product_cost

	def _count_total_price_on_page(self) -> list[float]:
		product_prices = self._driver.find_elements(By.XPATH, R_XPATH_PRODUCT_PRICE)

		result: list[float] = []
		for price in product_prices:
			p = float(''.join(x for x in price.text if x.isdigit() or x in [',', '.']))
			result.append(p)

		return result

	def _get_product_ids_on_current_page(self) -> list[int]:
		add_to_cart_btns = self._driver.find_elements(By.XPATH, R_XPATH_ADD_TO_CART)

		result: list[int] = list()
		for btn in add_to_cart_btns:
			id = int(btn.get_attribute('data-id'))
			result.append(id)

		return result

	__TABLE_D_IN_PRODUCT = 5

	def _get_product_table_rows(self) -> list[WebElement]:
		self.show_product_cart()

		result: list[WebElement] = []

		tries = 0
		while len(result) != len(self.__product_ids):
			cart_table_rows = self._driver.find_elements(By.XPATH, R_XPATH_TABLE_ROW_IN_CART)

			try:
				for row in cart_table_rows:
					table_d = row.find_elements(By.TAG_NAME, 'td')
					if len(table_d) == self.__TABLE_D_IN_PRODUCT:
						result.append(row)
			except:
				pass

			tries += 1
			if tries > self.__TRIES_UNTIL_CART_LOAD:
				break

		return result

	def _get_product_titles_on_current_page(self) -> list[str]:
		try:
			titles = self._driver.find_elements(By.XPATH, R_XPATH_PRODUCT_TITLE)
			result: list[str] = list()

			for title in titles:
				if len(title.text) != 0:
					result.append(title.text)

			return result
		except Exception as e:
			print(f"""
				  Failed web method: {__name__}
				  Exception: {e}
				  """)
			return []


__all__ = [
	'ProductCartMethods'
]
