from typing import Type, Optional

from selenium import webdriver

from selenium.webdriver import Chrome, ChromeOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement


class WebDriver:
	"""
	WebDriver wrapper
	"""

	_driver = None

	def __init__(self,
	             remote_web_driver: Type[RemoteWebDriver],
	             options: BaseOptions = None,
	             maximize_window_on_init: bool = True):

		if remote_web_driver is webdriver.Chrome:
			self._driver = webdriver.Chrome(options=options)

		if maximize_window_on_init:
			self._driver.maximize_window()

	def __delete__(self, instance):
		self._driver.close()

	def maximize_window(self):
		self._driver.maximize_window()
		
	def get(self, url: str) -> None:
		self._driver.get(url)

	@property
	def current_url(self) -> str:
		return self._driver.current_url

	def find_element(self, by: str = By.ID, value: Optional[str] = None) -> WebElement:
		return self._driver.find_element(by, value)

	def find_elements(self, by: str = By.ID, value: Optional[str] = None) -> list[WebElement]:
		return self._driver.find_elements(by, value)

	def implicitly_wait(self, time_to_wait: float) -> None:
		self._driver.implicitly_wait(time_to_wait)


__all__ = [
	'BaseOptions',
	'RemoteWebDriver',

	'Chrome',
	'ChromeOptions',

	'By',
	'WebElement',

	'WebDriver'
]
