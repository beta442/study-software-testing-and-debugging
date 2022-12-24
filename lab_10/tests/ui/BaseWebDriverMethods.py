from typing import Type

from tests.webdriver.WebDriver import\
	Chrome,\
	\
	BaseOptions,\
	RemoteWebDriver,\
	WebDriver


class BaseWebDriverMethods:
	_driver = None

	def __init__(self,
	             remote_web_driver: Type[RemoteWebDriver] = Chrome,
	             options: BaseOptions = None,
	             maximize_window_on_init: bool = True):
		self._driver = WebDriver(remote_web_driver=remote_web_driver,
		                         options=options,
		                         maximize_window_on_init=maximize_window_on_init)

	def get(self, url: str):
		self._driver.get(url)


__all__ = [
	'BaseWebDriverMethods'
]
