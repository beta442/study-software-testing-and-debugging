import requests
from typing import Optional
from sys import stderr

from rest_api.common import STATUS_CODE_OK
from rest_api.shop.body.addProduct import ModelAddProductBody
from rest_api.shop.common import ShopApiRouter, PK_ID
from rest_api.shop.model.product import \
	ModelProduct as product_model, \
	ModelProductList as product_list_model

from rest_api.shop.response.addProduct import ModelAddProductResponse
from rest_api.shop.response.removeProduct import ModelRemoveProductResponse


class ShopApi:
	@staticmethod
	def get_products() -> product_list_model:
		response = ShopApi.make_request(requests.get, ShopApiRouter.GET_ALL_PRODUCTS_URL)

		if response.status_code != STATUS_CODE_OK:
			raise Exception(f'Failed to get products. Response code is {response.status_code}')

		return product_list_model.parse_obj(response.json())

	@staticmethod
	def get_product_count() -> int:
		return len(ShopApi.get_products().__root__)

	@staticmethod
	def get_product(product_id) -> Optional[product_model]:
		products = ShopApi.get_products().__root__

		return next((product for product in products if product.id == product_id), None)

	@staticmethod
	def make_request(request: requests.request,
	                 url: str,
	                 params: Optional[dict] = None,
	                 json: Optional[dict] = None) -> requests.Response:
		try:
			return request(url, params=params, json=json)
		except Exception as e:
			print('Request exception:\n\t', e, file=stderr)

	@staticmethod
	def delete_product(product_id: int) -> ModelRemoveProductResponse:
		response = ShopApi.make_request(requests.get,
		                                ShopApiRouter.DELETE_PRODUCT_URL,
		                                {PK_ID: product_id})
		if response.status_code != STATUS_CODE_OK:
			raise Exception(f'Failed to delete product with id "{product_id}". Response code is {response.status_code}')
		return ModelRemoveProductResponse.parse_obj(response.json())

	@staticmethod
	def add_product(product: dict) -> ModelAddProductResponse:
		ModelAddProductBody.parse_obj(product)
		response = ShopApi.make_request(requests.post,
		                                ShopApiRouter.ADD_PRODUCT_URL,
		                                json=product)
		if response.status_code != STATUS_CODE_OK:
			raise Exception(f'Failed to add product. Response code is {response.status_code}')
		return ModelAddProductResponse.parse_obj(response.json())
