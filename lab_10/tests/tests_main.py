import unittest

from tests.common import VERBOSITY_LEVEL

from tests.ui.suite import TS_UI

from tests.ui.auth_pass.tests.test_go_to_login_page import TestCaseGoToLoginPage
from tests.ui.auth_pass.tests.test_auth import TestCaseAuth

TEST_SUITS = [
	TS_UI
]

if __name__ == '__main__':
	unittest.main(verbosity=VERBOSITY_LEVEL)
