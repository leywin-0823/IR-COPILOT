from typing import List

from app.attack.models import TechniqueHit


def map_techniques(events: List[dict]) -> List[TechniqueHit]:
    techniques: List[TechniqueHit] = []

    # ----------------------------
    # T1110 - Brute Force
    # ----------------------------
    failed_logins = [
        e for e in events
        if e.get("action") == "failed_login"
    ]

    if len(failed_logins) >= 3:
        techniques.append(
            TechniqueHit(
                technique_id="T1110",
                source="rule",
                confidence=0.8,
                evidence_event_ids=[
                    e.get("event_id") for e in failed_logins[:3] if e.get("event_id")
                ],
            )
        )

    return techniques
