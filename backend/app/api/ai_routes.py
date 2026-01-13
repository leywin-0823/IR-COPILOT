from fastapi import APIRouter, HTTPException
from app.ai.analyzer import analyze_events
from app.attack.mapper import map_techniques
from app.severity.scorer import calculate_severity
from app.response.recommender import recommend_response

router = APIRouter()

@router.post("/ai/analyze")
def ai_analyze(payload: dict):
    # -------------------------
    # 1. Input validation
    # -------------------------
    if "events" not in payload:
        raise HTTPException(
            status_code=400,
            detail="Request must include an 'events' array"
        )

    events = payload["events"]

    if not isinstance(events, list):
        raise HTTPException(
            status_code=400,
            detail="'events' must be a list"
        )

    if len(events) == 0:
        raise HTTPException(
            status_code=400,
            detail="'events' cannot be empty"
        )

    # -------------------------
    # 2. Run pipeline
    # -------------------------
    analysis = analyze_events(events)
    techniques = map_techniques(events)
    severity = calculate_severity(events, techniques)
    response = recommend_response(techniques, severity)

    # -------------------------
    # 3. Return unified result
    # -------------------------
    return {
        "analysis": analysis,
        "techniques": techniques,
        "severity": severity,
        "response": response,
        "errors": []
    }
