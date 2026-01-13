from app.report.markdown import render_markdown
from app.report.models import IncidentReport
from datetime import datetime

def test_markdown_contains_sections():
    report = IncidentReport(
        report_id="123",
        generated_at=datetime.utcnow(),
        executive_summary="Summary",
        severity="medium",
        techniques=["T1110"],
        indicators=["failed_login"],
        timeline=["event"],
        recommended_actions=["Review logs"],
        analyst_note="Analyst review required"
    )

    md = render_markdown(report)

    assert "# Incident Report" in md
    assert "## Executive Summary" in md
    assert "## Recommended Actions" in md
