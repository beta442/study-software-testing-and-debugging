PK_ID = 'id'
PK_CATEGORY_ID = 'category_id'
PK_TITLE = 'title'
PK_CONTENT = 'content'
PK_PRICE = 'price'
PK_OLD_PRICE = 'old_price'
PK_STATUS = 'status'
PK_KEYWORDS = 'keywords'
PK_DESCRIPTION = 'description'
PK_HIT = 'hit'

RK_STATUS = 'status'


class ShopApiRouter:
	"""
	Provides urls for interacting with
	shop's API
	"""

	_API_PRODUCT_ADD_KEY_POST_METHOD = 'add'
	_API_PRODUCT_DELETE_KEY_GET_METHOD = 'delete'
	_API_PRODUCT_EDIT_KEY_POST_METHOD = 'edit'
	_API_PRODUCT_GET_ALL_KEY_GET_METHOD = 'get_all'

	_API_PRODUCT_BRANCHES = {
		_API_PRODUCT_ADD_KEY_POST_METHOD: 'api/addproduct',
		_API_PRODUCT_DELETE_KEY_GET_METHOD: 'api/deleteproduct',
		_API_PRODUCT_EDIT_KEY_POST_METHOD: 'api/editproduct',
		_API_PRODUCT_GET_ALL_KEY_GET_METHOD: 'api/products',
	}

	BASE_URL = 'http://shop.qatl.ru/'

	ADD_PRODUCT_URL = BASE_URL + _API_PRODUCT_BRANCHES[_API_PRODUCT_ADD_KEY_POST_METHOD]
	DELETE_PRODUCT_URL = BASE_URL + _API_PRODUCT_BRANCHES[_API_PRODUCT_DELETE_KEY_GET_METHOD]
	EDIT_PRODUCT_URL = BASE_URL + _API_PRODUCT_BRANCHES[_API_PRODUCT_EDIT_KEY_POST_METHOD]
	GET_ALL_PRODUCTS_URL = BASE_URL + _API_PRODUCT_BRANCHES[_API_PRODUCT_GET_ALL_KEY_GET_METHOD]

	def get_delete_product_url(self, product_id):
		return self.DELETE_PRODUCT_URL + f'?{PK_ID}={product_id}'
