from typing import Type

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from selenium.webdriver import Chrome


class WebDriver:
	"""
	WebDriver wrapper
	"""

	_driver = None

	def __init__(self, remote_web_driver: Type[RemoteWebDriver]):
		if remote_web_driver is webdriver.Chrome:
			self._driver = webdriver.Chrome()

	def __del__(self):
		self._driver.close()


__all__ = [
	'RemoteWebDriver',

	'Chrome',

	'WebDriver'
]
