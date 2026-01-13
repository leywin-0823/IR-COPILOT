from pydantic import BaseModel
from typing import List, Literal


class TechniqueHit(BaseModel):
    technique_id: str
    source: Literal["rule", "ai"]
    confidence: float
    evidence_event_ids: List[str]
