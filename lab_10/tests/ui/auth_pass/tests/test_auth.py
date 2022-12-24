from typing import Union
from unittest import TestCase

from parameterized import parameterized

from tests.ui.auth_pass.web_driver_methods.AuthMethods import\
	AuthMethods as WebDriverMethods
from tests.webdriver.WebDriver import WebElement

from shop.ShopRouter import ShopRouter

from tests.ui.auth_pass.configs.loader import\
	TC_AUTHORIZE_JSON,\
	TC_AUTHORIZE_SUCCESS_JSON_KEY,\
	TC_AUTHORIZE_FAILURE_JSON_KEY,\
	F_LOGIN_KEY,\
	F_PASSWORD_KEY


class TestCaseAuth(TestCase):
	__webdriver_methods: WebDriverMethods = WebDriverMethods()
	__BASE_URL = ShopRouter.LOGIN_URL

	__login_field_form_group: Union[WebElement, None] = None
	__password_field_form_group: Union[WebElement, None] = None
	__login_field: Union[WebElement, None] = None
	__password_field: Union[WebElement, None] = None

	__submit_button: Union[WebElement, None] = None

	__CLASS_ATTRIBUTE_HAS_DANGER = 'has-danger'

	def setUp(self) -> None:
		self.__webdriver_methods.get(self.__BASE_URL)

		self.__login_field_form_group = self.__webdriver_methods.get_login_form_group()
		self.__password_field_form_group = self.__webdriver_methods.get_password_form_group()
		self.__login_field = self.__webdriver_methods.get_login_field()
		self.__password_field = self.__webdriver_methods.get_password_field()

		self.__submit_button = self.__webdriver_methods.get_submit_button()

	def test_login_page_on_dom_load(self):
		success_div = self.__webdriver_methods.get_success_div()
		error_div = self.__webdriver_methods.get_error_div()
		login_form_group = self.__login_field_form_group
		password_form_group = self.__password_field_form_group
		submit_button = self.__submit_button

		class_lfg = login_form_group.get_attribute('class')
		class_pfg = password_form_group.get_attribute('class')
		class_sb = submit_button.get_attribute('class')

		self.assertIs(error_div,
		              None,
		              f"""
		              Expected not to get error auth msg after DOM load
		              """)
		self.assertIs(success_div,
		              None,
		              f"""
		              Expected not to get success auth msg after DOM load
				      """)
		self.assertEqual(class_lfg.find(self.__CLASS_ATTRIBUTE_HAS_DANGER),
		                 -1,
		                 f"""
		                 Expected login form gorup's class without danger at {self.__BASE_URL} on DOM load
		                 Got {class_lfg}
		                 """)
		self.assertEqual(class_pfg.find(self.__CLASS_ATTRIBUTE_HAS_DANGER),
		                 -1,
		                 f"""
				         Expected login form gorup's class without danger at {self.__BASE_URL} on DOM load
				         Got {class_pfg}
				         """)
		self.assertNotEqual(class_sb.find('disabled'),
		                    -1,
		                    f"""
		                    Expected disabled in submit button' class at {self.__BASE_URL} on DOM load
		                    Got {class_sb}
		                    """)

	@parameterized.expand([
		'LOGIN',
		'PASSWORD'
	])
	def test_login_danger_data_in_input(self, input_field_type):
		is_type_login = (input_field_type == 'LOGIN')
		input_form_group = self.__login_field_form_group\
			if is_type_login\
			else self.__password_field_form_group

		self.__webdriver_methods.submit_user_login_and_password(login='', password='')

		class_lfg = input_form_group.get_attribute('class')

		self.assertNotEqual(class_lfg.find(self.__CLASS_ATTRIBUTE_HAS_DANGER),
		                    -1,
		                    f"""
		                    Expected to find danger in {input_field_type} form group's class at {self.__BASE_URL}
		                    after incorrect input
		                    Got {class_lfg}
		                    """)

	def test_submit_button_is_enabled_after_valid_input(self):
		login_input = self.__login_field
		login_form_group = self.__login_field_form_group
		password_input = self.__password_field
		password_form_group = self.__password_field_form_group
		submit_button = self.__submit_button

		login_input.send_keys('Test')
		password_input.send_keys('Test')

		class_lfg = login_form_group.get_attribute('class')
		self.assertEqual(class_lfg.find(self.__CLASS_ATTRIBUTE_HAS_DANGER),
		                 -1,
		                 f"""
		                 Expected not to find {self.__CLASS_ATTRIBUTE_HAS_DANGER} in login group's class attribute while
		                 entering valid input
		                 Got {class_lfg}
		                 """)
		class_pfg = password_form_group.get_attribute('class')
		self.assertEqual(class_pfg.find(self.__CLASS_ATTRIBUTE_HAS_DANGER),
		                 -1,
		                 f"""
				         Expected not to find {self.__CLASS_ATTRIBUTE_HAS_DANGER} in password group's class attribute while
				         entering valid input
				         Got {class_pfg}
				         """)
		class_sb = submit_button.get_attribute('class')
		self.assertEqual(class_sb.find('disabled'),
		                 -1,
		                 f"""
		                 Expected not to find "disabled" in submit button's class attribute
		                 Got {class_sb}
		                 """)

	@parameterized.expand([
		TC_AUTHORIZE_SUCCESS_JSON_KEY,

		TC_AUTHORIZE_FAILURE_JSON_KEY
	])
	def test_login(self, json_config_key):
		login_and_password_json_obj = TC_AUTHORIZE_JSON[json_config_key]

		self.__webdriver_methods.submit_user_login_and_password(login=login_and_password_json_obj[F_LOGIN_KEY],
		                                                        password=login_and_password_json_obj[F_PASSWORD_KEY])
		success_msg = self.__webdriver_methods.get_success_div()
		success = json_config_key in [
			TC_AUTHORIZE_SUCCESS_JSON_KEY
		]

		self.assertTrue(((success_msg is not None)
							if success
							else (success_msg is None)),
		                f"""
		                Expected {'not' if success else ''} to see success msg after
						{'good' if success_msg else 'bad'} inputs
		                """)


__all__ = [
	'TestCaseAuth'
]