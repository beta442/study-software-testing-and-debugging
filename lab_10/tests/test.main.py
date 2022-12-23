import unittest

from tests.common import VERBOSITY_LEVEL

from tests.ui.suite import TS_UI

TEST_SUITS = [
	TS_UI
]

if __name__ == '__main__':
	tests_runner = unittest.TextTestRunner(verbosity=VERBOSITY_LEVEL)

	for ts in TEST_SUITS:
		tests_runner.run(ts)
