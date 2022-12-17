import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


TC_ADD_PRODUCT_VALID_KEY = 'valid'
TC_ADD_PRODUCT_VALID_ALIAS_KEY = 'alias'

TC_ADD_PRODUCT_VALID_ALMOST_EMPTY_SCHEMA_KEY = 'almostEmptySchema'
TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID_KEY = 'withNotExistingId'
TC_ADD_PRODUCT_VALID_WITHOUT_ID_KEY = 'withoutId'

TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY = 'productTitleCollision'
TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY = 'productEmptyTitleCollision'


TC_ADD_PRODUCT_JSON = json.load(open(os.path.join(__location__, 'addProduct.json'), 'r'))
TC_ADD_PRODUCT_VALID_JSON = TC_ADD_PRODUCT_JSON[TC_ADD_PRODUCT_VALID_KEY]
TC_ADD_PRODUCT_VALID_ALIAS_JSON = TC_ADD_PRODUCT_JSON[TC_ADD_PRODUCT_VALID_ALIAS_KEY]

__all__ = [
    'TC_ADD_PRODUCT_JSON',
    'TC_ADD_PRODUCT_VALID_ALIAS_JSON',
    'TC_ADD_PRODUCT_VALID_JSON',

    'TC_ADD_PRODUCT_VALID_ALMOST_EMPTY_SCHEMA_KEY',
    'TC_ADD_PRODUCT_VALID_KEY',
    'TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID_KEY',
    'TC_ADD_PRODUCT_VALID_WITHOUT_ID_KEY',

    'TC_ADD_PRODUCT_VALID_PRODUCT_EMPTY_TITLE_COLLISION_KEY',
    'TC_ADD_PRODUCT_VALID_PRODUCT_TITLE_COLLISION_KEY',
]