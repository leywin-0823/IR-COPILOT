from pydantic import BaseModel
from typing import List
from datetime import datetime

class ReportSection(BaseModel):
    title: str
    content: str

class IncidentReport(BaseModel):
    report_id: str
    generated_at: datetime

    executive_summary: str
    severity: str

    techniques: List[str]
    indicators: List[str]

    timeline: List[str]

    recommended_actions: List[str]

    analyst_note: str
