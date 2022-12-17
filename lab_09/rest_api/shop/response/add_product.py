from pydantic import Field

from rest_api.shop.response.base import ModelBaseResponse


class ModelAddProductResponse(ModelBaseResponse):
	"""
	Add product response schema
	"""
	id: int = Field(description='Product''s id', gt=0)


__all__ = [
	'ModelAddProductResponse'
]
