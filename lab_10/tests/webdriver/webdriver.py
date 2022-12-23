from typing import Type

from selenium import webdriver
from selenium.webdriver.common.options import BaseOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from selenium.webdriver import Chrome, ChromeOptions


class WebDriver:
	"""
	WebDriver wrapper
	"""

	_driver = None

	def __init__(self, remote_web_driver: Type[RemoteWebDriver], options: BaseOptions = None):
		if remote_web_driver is webdriver.Chrome:
			self._driver = webdriver.Chrome(options=options)

	def __del__(self):
		self._driver.close()


__all__ = [
	'BaseOptions',
	'RemoteWebDriver',

	'Chrome',
	'ChromeOptions',

	'WebDriver'
]
