import unittest

from tests.ui.auth_pass.tests.test_auth import AuthTest

TEST_LOADER = unittest.TestLoader()

TC_AUTH = TEST_LOADER.loadTestsFromTestCase(AuthTest)

TS_UI = unittest.TestSuite([TC_AUTH])

__all__ = [
	'TS_UI'
]
