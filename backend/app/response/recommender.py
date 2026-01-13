from app.attack.models import TechniqueHit
from app.severity.models import SeverityResult
from app.response.models import ResponsePlan


def recommend_response(
    techniques: list[TechniqueHit],
    severity: SeverityResult,
) -> ResponsePlan:

    containment = []
    investigation = []
    recovery = []

    # --- Investigation is always safe ---
    investigation.append("Review authentication logs for related activity")

    # --- Technique-specific containment ---
    technique_ids = {t.technique_id for t in techniques}

    if "T1110" in technique_ids and severity.level in ("high", "critical"):
        containment.append("Temporarily disable or lock affected user accounts")
        containment.append("Block source IP addresses associated with failed attempts")

    if severity.level in ("medium",):
        containment.append("Increase monitoring for affected accounts")

    # --- Recovery guidance ---
    if severity.level in ("high", "critical"):
        recovery.append("Force password resets for affected accounts")
        recovery.append("Validate no unauthorized changes were made")

    return ResponsePlan(
        severity=severity.level,
        containment=containment,
        investigation=investigation,
        recovery=recovery,
        analyst_note=(
            "These recommendations are advisory only. "
            "An analyst must review and approve all response actions."
        ),
    )
