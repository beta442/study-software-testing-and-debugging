import os
import json

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


TC_ADD_PRODUCT_VALID_KEY = 'valid'
TC_ADD_PRODUCT_VALID_WITH_NOT_EXISTING_ID = 'validWithNotExistingId'
TC_ADD_PRODUCT_VALID_WITHOUT_ID = 'validWithoutId'


TC_ADD_PRODUCT_JSON = json.load(open(os.path.join(__location__, 'addProduct.json'), 'r'))
