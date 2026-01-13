from pydantic import BaseModel
from typing import List

class AttackTechnique(BaseModel):
    technique_id: str       # e.g. "T1110"
    name: str               # "Brute Force"
    tactics: List[str]      # ["credential_access"]
    description: str
    detection_notes: str
