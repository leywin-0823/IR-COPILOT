from app.report.models import IncidentReport

def render_markdown(report: IncidentReport) -> str:
    return f"""
# Incident Report

**Report ID:** {report.report_id}  
**Generated:** {report.generated_at.isoformat()}  
**Severity:** **{report.severity.upper()}**

---

## Executive Summary
{report.executive_summary}

---

## MITRE ATT&CK Techniques
{chr(10).join(f"- {t}" for t in report.techniques)}

---

## Indicators
{chr(10).join(f"- {i}" for i in report.indicators)}

---

## Timeline
{chr(10).join(f"- {t}" for t in report.timeline)}

---

## Recommended Actions
{chr(10).join(f"- {a}" for a in report.recommended_actions)}

---

## Analyst Note
{report.analyst_note}
""".strip()
