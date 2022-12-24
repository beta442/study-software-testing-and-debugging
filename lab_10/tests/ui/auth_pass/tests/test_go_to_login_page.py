from typing import Union
from unittest import TestCase

from tests.ui.auth_pass.web_driver_methods.GoToLoginPageMethods import\
	GoToLoginPageMethods as WebDriverMethods,\
	By,\
	R_XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU
from tests.webdriver.WebDriver import WebElement

from shop.ShopRouter import ShopRouter


class TestCaseGoToLoginPage(TestCase):
	f"""
	Authorization UI tests on the shop's website
	"""

	__webdriver_methods: WebDriverMethods = WebDriverMethods()
	__BASE_URL = ShopRouter.BASE_URL

	__account_button: Union[WebElement, None] = None
	__account_dropdown_menu: Union[WebElement, None] = None
	__login_button: Union[WebElement, None] = None

	def setUp(self) -> None:
		self.__webdriver_methods.get(self.__BASE_URL)

		self.__account_button = self.__webdriver_methods.get_account_dropdown_button()
		self.__account_dropdown_menu = self.__webdriver_methods.get_account_dropdown_menu()
		self.__login_button = self.__webdriver_methods.get_login_button()

	def test_account_button_exists(self):
		button = self.__account_button

		self.assertIsNot(button,
		                 None,
		                 f"""
		                 Expected to find Account dropdown button at {self.__BASE_URL}
		                 Got None 
		                 """)
		self.assertTrue(button.is_displayed(),
		                f"""
		                Expected to find displayed Account dropdown button at {self.__BASE_URL}
		                Got {button.__str__()} 
		                """)

	def test_account_dropdown_menu_exists(self):
		dropdown_menu = self.__account_dropdown_menu

		self.assertIsNot(dropdown_menu,
		                 None,
		                 f"""
		                 Expected to find Account dropdown menu in DOM at {self.__BASE_URL}
		                 """)
		self.assertFalse(dropdown_menu.is_displayed(),
		                 f"""
		                 Expected not visible Account dropdown menu at {self.__BASE_URL}
		                 """)

	def test_click_account_button_toggles_showing_dropdown_menu(self):
		button = self.__account_button
		dropdown_menu = self.__account_dropdown_menu

		button.click()
		self.assertTrue(dropdown_menu.is_displayed(),
		                f"""
		                Expected to see Account dropdown menu after click on Account button at {self.__BASE_URL}
		                """)

		button.click()
		self.assertFalse(dropdown_menu.is_displayed(),
		                 f"""
				         Expected not to see Account dropdown menu after click on Account button at {self.__BASE_URL}
				         """)

	def test_login_button_is_in_dropdown_menu(self):
		dropdown_menu = self.__account_dropdown_menu
		login_button = None
		try:
			login_button = dropdown_menu.find_element(By.XPATH, R_XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU)
		except Exception:
			pass

		self.assertIsNot(login_button,
		                 None,
		                 """
		                 Expected to find login button inside account's dropdown menu
		                 """)

	def test_login_button_displayed_after_click_on_account_button(self):
		account_button = self.__account_button
		login_button = self.__login_button
		account_button.click()

		self.assertTrue(login_button.is_displayed(),
		                f"""
				        Expected to see login button after click at Account button at {self.__BASE_URL}
				        """)

	def test_click_login_button_in_account_dropdown_menu_routes_to_login_page(self):
		# Need to open Account dropdown menu first
		self.__account_button.click()
		self.__login_button.click()
		current_url = self.__webdriver_methods.get_current_url()

		self.assertEqual(ShopRouter.LOGIN_URL,
		                 current_url,
		                 f"""
		                 Expected to be at {ShopRouter.LOGIN_URL} after clicking at login button
		                 Got {current_url} url
		                 """)


__all__ = [
	'TestCaseGoToLoginPage'
]
