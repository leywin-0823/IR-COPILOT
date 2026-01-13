from pydantic import BaseModel, Field

class IngestRequest(BaseModel):
    logs: str = Field(..., min_length=1, description="Raw log text")
