import requests

from sys import stderr

from shop.api.common import ShopApiRouter, STATUS_CODE_OK
from shop.api.models.product import ModelProduct as product_model


class ShopApi:
	@staticmethod
	def get_products() -> list[product_model]:
		return ShopApi.make_request(requests.get, ShopApiRouter.GET_ALL_PRODUCTS_URL).json()

	@staticmethod
	def make_request(request, url, params=None) -> requests.Response:
		try:
			return request(url, params=params)
		except Exception as e:
			print('Request exception:\n\t', e, file=stderr)

	@staticmethod
	def delete_product(product_id) -> requests.Response:
		response = ShopApi.make_request(requests.get,
		                                ShopApiRouter.DELETE_PRODUCT_URL,
		                                {product_model.get_id_key(): product_id})
		if response.status_code != STATUS_CODE_OK:
			raise Exception(f'Failed to delete product with id "{product_id}"')
		return response
