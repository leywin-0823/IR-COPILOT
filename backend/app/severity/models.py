from pydantic import BaseModel
from typing import List

class SeverityBreakdown(BaseModel):
    factor: str
    score: int
    reason: str

class SeverityResult(BaseModel):
    score: int
    level: str
    breakdown: List[SeverityBreakdown]
