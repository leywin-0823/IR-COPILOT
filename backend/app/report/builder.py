from datetime import datetime
from uuid import uuid4

from app.report.models import IncidentReport
from app.attack.models import TechniqueHit
from app.response.models import ResponsePlan
from app.severity.models import SeverityResult

def build_incident_report(
    summary: str,
    severity: SeverityResult,
    techniques: list[TechniqueHit],
    response: ResponsePlan,
    events: list[dict],
) -> IncidentReport:

    return IncidentReport(
        report_id=str(uuid4()),
        generated_at=datetime.utcnow(),

        executive_summary=summary,
        severity=severity.level,

        techniques=[
            f"{t.technique_id} ({t.source})"
            for t in techniques
        ],

        indicators=[
            f"{e.get('action')} from {e.get('source_ip', 'unknown')}"
            for e in events
        ],

        timeline=[
            f"{e.get('timestamp', 'unknown')} – {e.get('action')}"
            for e in events
        ],

        recommended_actions=[
            *response.containment,
            *response.investigation,
            *response.recovery,
        ],

        analyst_note=response.analyst_note,
    )
