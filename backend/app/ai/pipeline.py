from app.ai.analyzer import analyze_events
from app.attack.mapper import map_techniques
from app.severity.scorer import calculate_severity
from app.response.recommender import recommend_response


def analyze_incident(events: list[dict]):
    # Phase 2 — AI analysis
    ai_result = analyze_events(events)

    # Phase 3.1 — ATT&CK mapping
    techniques = map_techniques(events)

    # Phase 3.2/3.3 — Severity
    severity_result = calculate_severity(events, techniques)

    # Phase 3.4 — Response guidance ✅
    response_plan = recommend_response(
        techniques=techniques,
        severity=severity_result,
    )

    return {
        "analysis": ai_result,
        "techniques": techniques,
        "severity": severity_result,
        "response": response_plan,
    }
