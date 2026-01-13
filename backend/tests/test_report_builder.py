from app.report.builder import build_incident_report
from app.severity.models import SeverityResult
from app.attack.models import TechniqueHit
from app.response.models import ResponsePlan

def test_report_contains_core_sections():
    report = build_incident_report(
        summary="Test incident",
        severity=SeverityResult(score=80, level="high", breakdown=[]),
        techniques=[
            TechniqueHit(
                technique_id="T1110",
                source="rule",
                confidence=0.9,
                evidence_event_ids=["1"]
            )
        ],
        response=ResponsePlan(
            severity="high",
            containment=["Disable account"],
            investigation=["Review authentication logs"],
            recovery=[],
            analyst_note="Analyst review required"
        ),
        events=[
            {
                "timestamp": "2026-01-09T19:20:48Z",
                "action": "failed_login",
                "source_ip": "10.0.0.5"
            }
        ]
    )

    assert report.severity == "high"
    assert "T1110" in report.techniques[0]
    assert len(report.timeline) == 1
