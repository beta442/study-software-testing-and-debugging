from unittest import TestCase

from tests.ui.auth_pass.web_driver_methods.AuthMethods import AuthMethods as WebDriverMethods

class AuthTest(TestCase):
	f"""
	Authorization UI tests on the shop's website
	"""

	__webdriver_methods: WebDriverMethods = WebDriverMethods()

	def test_eq(self):
		self.assertEqual(1, 1)
