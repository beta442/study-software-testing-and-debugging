from pydantic import BaseModel, Field
from typing import Optional


PRODUCT_CATEGORY_ID_MIN = 1
PRODUCT_CATEGORY_ID_MAX = 14


class ModelBaseProduct(BaseModel):
	"""
	Shop''s REST API base product model
	"""
	category_id: int = Field(description='Product''s category id',
	                         ge=PRODUCT_CATEGORY_ID_MIN,
	                         le=PRODUCT_CATEGORY_ID_MAX)
	old_price: float = Field(description='Product''s old price', ge=0)
	price: float = Field(description='Product''s actual price', ge=0)
	title: str = Field(description='Product''s title')



__all__ = [
	'PRODUCT_CATEGORY_ID_MIN',
	'PRODUCT_CATEGORY_ID_MAX',

	'ModelBaseProduct'
]
