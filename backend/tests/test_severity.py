from app.severity.scorer import calculate_severity
from app.attack.models import TechniqueHit

def test_bruteforce_severity_high():
    events = [
        {"event_id": "1", "action": "failed_login", "user": "root"},
        {"event_id": "2", "action": "failed_login", "user": "root"},
        {"event_id": "3", "action": "failed_login", "user": "root"},
        {"event_id": "4", "action": "failed_login", "user": "root"},
        {"event_id": "5", "action": "failed_login", "user": "root"},
    ]

    techniques = [
        TechniqueHit(
            technique_id="T1110",
            source="rule",
            confidence=0.8,
            evidence_event_ids=["1", "2", "3"]
        )
    ]

    result = calculate_severity(events, techniques)

    assert result.level in ("high", "critical")
    assert result.score >= 90
    assert len(result.breakdown) > 0
