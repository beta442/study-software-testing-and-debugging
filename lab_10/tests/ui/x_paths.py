from shop.ShopRouter import ShopRouter

# LOGIN PAGE

R_XPATH_LOGIN_PAGE_AUTH_ERROR = '//div[@class = "alert alert-danger"]'
R_XPATH_LOGIN_PAGE_AUTH_SUCCESS = '//div[@class = "alert alert-success"]'
R_XPATH_LOGIN_PAGE_FORM_GROUP_FOR_INPUT_FIELD = '//div[contains(@class, "form-group has-feedback")]'
R_XPATH_LOGIN_PAGE_LOGIN_INPUT_FIELD = '//input[@name = "login"]'
R_XPATH_LOGIN_PAGE_PASSWORD_INPUT_FIELD = '//input[@name = "password"]'
R_XPATH_LOGIN_PAGE_REGISTER_MAIN = '//div[@class = "register-main"]'
R_XPATH_LOGIN_PAGE_SUBMIT_BUTTON = '//button[@type = "submit"][contains(@class, "btn btn-default")]'

XPATH_LOGIN_PAGE_FORM_GROUP_FOR_INPUT_FIELD =\
	R_XPATH_LOGIN_PAGE_REGISTER_MAIN + R_XPATH_LOGIN_PAGE_FORM_GROUP_FOR_INPUT_FIELD
XPATH_LOGIN_PAGE_LOGIN_INPUT_FIELD =\
	R_XPATH_LOGIN_PAGE_REGISTER_MAIN + R_XPATH_LOGIN_PAGE_LOGIN_INPUT_FIELD
XPATH_LOGIN_PAGE_PASSWORD_INPUT_FIELD =\
	R_XPATH_LOGIN_PAGE_REGISTER_MAIN + R_XPATH_LOGIN_PAGE_PASSWORD_INPUT_FIELD
XPATH_LOGIN_PAGE_SUBMIT_BUTTON =\
	R_XPATH_LOGIN_PAGE_REGISTER_MAIN + R_XPATH_LOGIN_PAGE_SUBMIT_BUTTON

# HOME PAGE

R_XPATH_AUTH_BTN_GROUP = '//div[@class = "btn-group"]'
R_XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU = f'//a[@href = "{ShopRouter.ROUTE_LOGIN}"]'

XPATH_AUTH_ACCOUNT_BUTTON = R_XPATH_AUTH_BTN_GROUP + '/a[@class = "dropdown-toggle"]'
XPATH_AUTH_ACCOUNT_DROPDOWN_MENU = R_XPATH_AUTH_BTN_GROUP + '/ul[@class = "dropdown-menu"]'
XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU =\
	XPATH_AUTH_ACCOUNT_DROPDOWN_MENU + R_XPATH_AUTH_LOGIN_IN_ACCOUNT_DROPDOWN_MENU

# PRODUCT CART

R_XPATH_MODAL_CONTENT = '//div[@class = "modal-content"]'
R_XPATH_MODAL_BODY = '//div[@class = "modal-body"]'

R_XPATH_CART_SHOW_BTN = '//a[@href = "cart/show"]'

R_XPATH_CART_CLOSE_BTN = f'{R_XPATH_MODAL_CONTENT}//button[@type = "button" and @class = "close"]'
R_XPATH_CART_CLEAR_BTN = f'{R_XPATH_MODAL_CONTENT}//button[@onClick = "clearCart()"]'
R_XPATH_CART_TOTAL_PRICE = f'{R_XPATH_MODAL_CONTENT}//td[contains(@class, "cart-sum")]'
R_XPATH_CART_PRODUCT_DELETE_SPAN = f'{R_XPATH_MODAL_CONTENT}//span[contains(@class, "del-item")]'
R_XPATH_TABLE_ROW_IN_CART = f'{R_XPATH_MODAL_CONTENT}{R_XPATH_MODAL_BODY}//tr'

R_XPATH_ADD_TO_CART = '//a[@href = "cart/add?id={item_id}" or @class = "add-to-cart-link"]'
R_XPATH_PRODUCT_PRICE = '//span[contains(@class, "item_price")]'

R_XPATH_PRODUCT_TITLE = '//div[@class = "product-bottom"]//a'
