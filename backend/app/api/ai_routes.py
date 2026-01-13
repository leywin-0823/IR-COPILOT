from fastapi import APIRouter
from app.ai.analyzer import analyze_events
from app.attack.mapper import map_techniques
from app.severity.scorer import calculate_severity
from app.response.recommender import recommend_response
from app.core.errors import AnalysisError

router = APIRouter()

@router.post("/ai/analyze")
def analyze(payload: dict):
    errors: list[AnalysisError] = []

    analysis = None
    techniques = []
    severity = None
    response_plan = None

    # Phase 2 — AI analysis
    try:
        analysis = analyze_events(payload["events"])
    except Exception as e:
        errors.append(
            AnalysisError(
                component="analysis",
                message=str(e),
            )
        )

    # Phase 3.1 — ATT&CK mapping
    try:
        techniques = map_techniques(payload["events"])
    except Exception as e:
        errors.append(
            AnalysisError(
                component="attack_mapping",
                message=str(e),
            )
        )

    # Phase 3.2 — Severity
    try:
        severity = calculate_severity(payload["events"], techniques)
    except Exception as e:
        errors.append(
            AnalysisError(
                component="severity",
                message=str(e),
            )
        )

    # Phase 3.4 — Response
    try:
        if severity:
            response_plan = recommend_response(techniques, severity)
    except Exception as e:
        errors.append(
            AnalysisError(
                component="response",
                message=str(e),
            )
        )

    return {
        "analysis": analysis,
        "techniques": techniques,
        "severity": severity,
        "response": response_plan,
        "errors": errors,
    }
