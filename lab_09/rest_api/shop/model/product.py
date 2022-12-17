from typing import Optional
from pydantic import BaseModel, Field

from rest_api.shop.model.base_product import ModelBaseProduct


PRODUCT_ALIAS_POSTFIX = '-0'


class ModelProduct(ModelBaseProduct):
	"""
	Product Model
	Defines the attributes of a product
	"""

	alias: str = Field(description="""
		                   Product''s alias.
		                   Equal to title{}. {} is (-0)*, if alias exists
		                   """)
	cat: str = Field(description='The catalog title where the product is located',
	                 min_length=1)
	hit: int = Field(description='Product''s hit status',
	                 ge=0)
	id: int = Field(description='Product''s id',
	                ge=0)
	img: str = Field(description='Product''s image url',
	                 min_length=0)
	status: int = Field(description='Is product 0 or 1',
	                    ge=0,
	                    le=1)

	content: Optional[str] = Field(description='Product''s content')
	description: Optional[str] = Field(description='Product''s description')
	keywords: Optional[str] = Field(description='Products''s keywords')


class ModelProductList(BaseModel):
	__root__: list[ModelProduct]


__all__ = [
	'PRODUCT_ALIAS_POSTFIX',

	'ModelProduct',
	'ModelProductList'
]
