import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

TC_AUTHORIZE_JSON = json.load(open(os.path.join(__location__, 'authorize.json'), 'r'))

TC_AUTHORIZE_FAILURE_JSON_KEY = 'failure'
TC_AUTHORIZE_SUCCESS_JSON_KEY = 'success'

F_LOGIN_KEY = 'login'
F_PASSWORD_KEY = 'password'

__all__ = [
	'TC_AUTHORIZE_JSON',

	'TC_AUTHORIZE_FAILURE_JSON_KEY',
	'TC_AUTHORIZE_SUCCESS_JSON_KEY',

	'F_LOGIN_KEY',
	'F_PASSWORD_KEY'
]
