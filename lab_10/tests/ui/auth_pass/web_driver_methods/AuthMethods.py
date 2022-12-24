from typing import Union

from tests.ui.BaseWebDriverMethods import BaseWebDriverMethods

from tests.ui.common import BOOL_MAKE_WEBDRIVER_HEADLESS, WEB_DRIVER_ARG_HEADLESS
from tests.webdriver.WebDriver import By, ChromeOptions, WebElement

from tests.ui.x_paths import *


class AuthMethods(BaseWebDriverMethods):
	"""
	WebDriver's methods for shop's auth UI tests
	"""

	def __init__(self):
		options = None
		if BOOL_MAKE_WEBDRIVER_HEADLESS:
			options = ChromeOptions()
			options.add_argument(WEB_DRIVER_ARG_HEADLESS)

		super(AuthMethods, self).__init__(options=options)

	def get_error_div(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, R_XPATH_LOGIN_PAGE_AUTH_ERROR)
		except Exception:
			return None

	def get_success_div(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, R_XPATH_LOGIN_PAGE_AUTH_SUCCESS)
		except Exception:
			return None

	def get_login_field(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_LOGIN_INPUT_FIELD)
		except Exception:
			return None

	def get_password_field(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_PASSWORD_INPUT_FIELD)
		except Exception:
			return None

	def get_submit_button(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_element(By.XPATH, XPATH_LOGIN_PAGE_SUBMIT_BUTTON)
		except Exception:
			return None

	def get_login_form_group(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_elements(By.XPATH, XPATH_LOGIN_PAGE_FORM_GROUP_FOR_INPUT_FIELD)[0]
		except Exception:
			return None

	def get_password_form_group(self) -> Union[WebElement, None]:
		try:
			return self._driver.find_elements(By.XPATH, XPATH_LOGIN_PAGE_FORM_GROUP_FOR_INPUT_FIELD)[1]
		except Exception:
			return None

	def submit_user_login_and_password(self, login, password):
		login_field = self.get_login_field()
		password_field = self.get_password_field()
		submit_bt = self.get_submit_button()

		login_field.send_keys(login)
		password_field.send_keys(password)
		submit_bt.click()

__all__ = [
	'AuthMethods'
]
