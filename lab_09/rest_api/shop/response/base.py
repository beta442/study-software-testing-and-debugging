from pydantic import BaseModel, Field


class ModelBaseResponse(BaseModel):
	status: int = Field(description='Execution status', ge=0, le=1)
