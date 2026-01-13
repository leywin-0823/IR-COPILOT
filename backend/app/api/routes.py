from fastapi import APIRouter
from app.ai.analyzer import analyze_events

router = APIRouter()

@router.post("/ai/analyze")
def ai_analyze(events: list[dict]):
    result = analyze_events(events)
    return result
