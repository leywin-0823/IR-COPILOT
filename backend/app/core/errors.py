from pydantic import BaseModel

class AnalysisError(BaseModel):
    component: str
    message: str
    recoverable: bool = True
