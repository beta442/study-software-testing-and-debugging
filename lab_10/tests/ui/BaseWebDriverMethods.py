from typing import Type

from tests.webdriver.webdriver import\
	Chrome,\
	\
	RemoteWebDriver,\
	WebDriver


class BaseWebDriverMethods:
	_driver = None

	def __init__(self, remote_web_driver: Type[RemoteWebDriver] = Chrome):
		self._driver = WebDriver(remote_web_driver)


__all__ = [
	'BaseWebDriverMethods'
]
