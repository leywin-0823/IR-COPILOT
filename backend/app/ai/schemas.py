from pydantic import BaseModel
from typing import List, Dict, Any

class EvidenceItem(BaseModel):
    event_id: str
    timestamp: str
    field: str
    value: str

class Confidence(BaseModel):
    level: str  # low | medium | high
    reasoning: str

class AISummary(BaseModel):
    title: str
    narrative: str

class AIAnalysis(BaseModel):
    what_happened: str
    why_it_matters: str
    attack_stage: str

class AIResult(BaseModel):
    summary: AISummary
    analysis: AIAnalysis
    evidence: List[EvidenceItem]
    confidence: Confidence
