from app.response.recommender import recommend_response
from app.attack.models import TechniqueHit
from app.severity.models import SeverityResult


def test_high_severity_bruteforce_response():
    techniques = [
        TechniqueHit(
            technique_id="T1110",
            source="rule",
            confidence=0.9,
            evidence_event_ids=["1", "2", "3"]
        )
    ]

    severity = SeverityResult(
        score=85,
        level="high",
        breakdown=[]
    )

    response = recommend_response(techniques, severity)

    assert response.severity == "high"
    assert any("disable" in step.lower() for step in response.containment)
    assert any(
        "review authentication logs" in step.lower()
        for step in response.investigation
    )
    assert "analyst" in response.analyst_note.lower()


def test_medium_severity_response_is_non_disruptive():
    techniques = [
        TechniqueHit(
            technique_id="T1110",
            source="rule",
            confidence=0.6,
            evidence_event_ids=["1"]
        )
    ]

    severity = SeverityResult(
        score=50,
        level="medium",
        breakdown=[]
    )

    response = recommend_response(techniques, severity)

    assert not any("disable" in step.lower() for step in response.containment)
    assert any("monitor" in step.lower() or "review" in step.lower()
               for step in response.investigation)

def test_unknown_technique_safe_response():
    techniques = []
    severity = SeverityResult(score=30, level="low", breakdown=[])

    response = recommend_response(techniques, severity)

    assert response.severity == "low"
    assert response.containment == []
    assert len(response.investigation) > 0

def test_response_schema_contract():
    response = recommend_response(
        [],
        SeverityResult(score=10, level="low", breakdown=[])
    )

    assert hasattr(response, "severity")
    assert hasattr(response, "containment")
    assert hasattr(response, "investigation")
    assert hasattr(response, "recovery")
    assert hasattr(response, "analyst_note")
