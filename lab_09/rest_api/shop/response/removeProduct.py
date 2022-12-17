from pydantic import BaseModel, Field


class ModelRemoveProductResponse(BaseModel):
	status: int = Field(description='Execution status', ge=0, le=1)
