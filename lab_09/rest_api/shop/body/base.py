from pydantic import BaseModel, Field

PRODUCT_CATEGORY_ID_MIN = 1
PRODUCT_CATEGORY_ID_MAX = 15


class ModelBaseRequestProductBody(BaseModel):
	"""
	Shop's REST API base request product body's schema
	"""
	category_id: int = Field(description='Product''s category',
	                         ge=PRODUCT_CATEGORY_ID_MIN,
	                         le=PRODUCT_CATEGORY_ID_MAX)
	title: str = Field(description='Product''s title')
	price: float = Field(description='Product''s actual price',
	                     ge=0)
	old_price: float = Field(description='Product''s old price',
	                         ge=0)


__all__ = [
	'PRODUCT_CATEGORY_ID_MIN',
	'PRODUCT_CATEGORY_ID_MAX',

	'ModelBaseRequestProductBody',
]
