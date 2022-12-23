from typing import Type

from tests.webdriver.webdriver import\
	Chrome,\
	\
	BaseOptions,\
	RemoteWebDriver,\
	WebDriver


class BaseWebDriverMethods:
	_driver = None

	def __init__(self, remote_web_driver: Type[RemoteWebDriver] = Chrome, options: BaseOptions = None):
		self._driver = WebDriver(remote_web_driver, options)


__all__ = [
	'BaseWebDriverMethods'
]
