from tests.ui.BaseWebDriverMethods import BaseWebDriverMethods

from tests.ui.common import WEB_DRIVER_ARG_HEADLESS
from tests.webdriver.webdriver import ChromeOptions


class AuthMethods(BaseWebDriverMethods):
	"""
	WebDriver's methods for shop's auth UI tests
	"""

	def __init__(self):
		options = ChromeOptions()
		options.add_argument(WEB_DRIVER_ARG_HEADLESS)

		super(AuthMethods, self).__init__(options=options)


__all__ = [
	'AuthMethods'
]
