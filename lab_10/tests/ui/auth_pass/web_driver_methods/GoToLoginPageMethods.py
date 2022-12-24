from typing import Union

from tests.ui.BaseWebDriverMethods import BaseWebDriverMethods

from tests.ui.common import BOOL_MAKE_WEBDRIVER_HEADLESS, WEB_DRIVER_ARG_HEADLESS
from tests.webdriver.WebDriver import By, ChromeOptions, WebElement

from tests.ui.x_paths import *


class GoToLoginPageMethods(BaseWebDriverMethods):
	"""
	WebDriver's methods for shop's go to login page UI tests
	"""

	def __init__(self):
		options = None
		if BOOL_MAKE_WEBDRIVER_HEADLESS:
			options = ChromeOptions()
			options.add_argument(WEB_DRIVER_ARG_HEADLESS)

		super(GoToLoginPageMethods, self).__init__(options=options)

	def get_account_dropdown_button(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_AUTH_ACCOUNT_BUTTON)
		except Exception:
			return None

	def get_account_dropdown_menu(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_AUTH_ACCOUNT_DROPDOWN_MENU)
		except Exception:
			return None

	def get_login_button(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU)
		except Exception:
			return None

	def get_current_url(self) -> str:
		return self._driver.current_url


__all__ = [
	'GoToLoginPageMethods',

	'By',
	'R_XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU'
]
