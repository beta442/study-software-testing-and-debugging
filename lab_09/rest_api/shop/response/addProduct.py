from pydantic import BaseModel, Field


class ModelAddProductResponse(BaseModel):
	"""
	Add product response schema
	"""

	id: int = Field(description='Product''s id', gt=0)
	status: int = Field(description='Execution status', ge=0, le=1)
