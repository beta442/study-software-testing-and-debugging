import unittest

from tests.ui.auth_pass.tests.test_go_to_login_page import TestCaseGoToLoginPage
from tests.ui.auth_pass.tests.test_auth import TestCaseAuth

TEST_LOADER = unittest.TestLoader()

TC_AUTH = TEST_LOADER.loadTestsFromTestCase(TestCaseAuth)
TC_GO_TO_LOGIN_PAGE = TEST_LOADER.loadTestsFromTestCase(TestCaseGoToLoginPage)

TS_UI = unittest.TestSuite([
	TC_GO_TO_LOGIN_PAGE,
	TC_AUTH,
])

__all__ = [
	'TS_UI'
]
