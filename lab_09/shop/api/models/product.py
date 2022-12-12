from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class ModelProduct(BaseModel):
	"""
	Product Model
	Defines the attributes of a product
	"""

	alias: str = Field(description="""
		                   Product''s alias.
		                   Equal to title{}. {} is _*, where * is digit, if alias exists or empty if not
		                   """,
	                   min_length=1)
	cat: str = Field(description='The catalog title where the product is located',
	                 min_length=1)
	category_id: int = Field(description='Product''s category id',
	                         ge=1,
	                         le=15)
	content: Optional[str] = Field(description='Product''s content')
	description: Optional[str] = Field(description='Product''s description')
	hit: int = Field(description='I don''t give a fuck',
	                 ge=0)
	id: int = Field(description='Product''s id',
	                ge=0)
	img: str = Field(description='Product''s image url',
	                 min_length=0)
	keywords: Optional[str] = Field(description='Products''s keywords')
	old_price: float = Field(description='Product''s old price', ge=0)
	price: float = Field(description='Product''s actual price', ge=0)
	status: str = Field(description='Is product 0 or 1', regex='0|1')
	title: str = Field(description='Product''s title', min_length=1)

	@staticmethod
	def get_id_key():
		return 'id'
