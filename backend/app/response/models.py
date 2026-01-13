from pydantic import BaseModel
from typing import List, Literal


class ResponseAction(BaseModel):
    action_type: Literal["investigation", "containment", "recovery"]
    title: str
    description: str
    justification: str
    related_techniques: List[str]


class ResponsePlan(BaseModel):
    severity: Literal["low", "medium", "high", "critical"]

    containment: List[str] = []
    investigation: List[str] = []
    recovery: List[str] = []

    analyst_note: str
