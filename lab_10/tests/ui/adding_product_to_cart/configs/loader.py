import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

TC_CART_TEST_JSON = json.load(open(os.path.join(__location__, 'cart_test.json'), 'r'))

TC_ADD_SINGLE_PRODUCT = 'addSingleProduct'

F_URL_KEY = 'url'

__all__ = [
	'TC_CART_TEST_JSON',

	'TC_ADD_SINGLE_PRODUCT',

	'F_URL_KEY'
]