from pydantic import Field
from typing import Optional

from rest_api.shop.body.base import ModelBaseRequestProductBody


class ModelEditProductBody(ModelBaseRequestProductBody):
	"""
	Shop's REST API EditProduct branch body's schema
	"""

	id: int = Field(description='Product''s id', gt=0)

	keywords: Optional[str] = Field(description='Product''s keywords')
	description: Optional[str] = Field()
	hit: Optional[int] = Field(description='Product''s hit status',
	                           ge=0,
	                           le=1)
	status: Optional[int] = Field(description='Product''s status',
	                              ge=0,
	                              le=1)
	content: Optional[str] = Field(description='Product''s content')


__all__ = [
	'ModelEditProductBody',
]
