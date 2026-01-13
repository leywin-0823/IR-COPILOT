from typing import List, Dict
from app.attack.models import TechniqueHit

def map_attack_techniques(events: List[Dict]) -> List[TechniqueHit]:
    hits: List[TechniqueHit] = []

    # Rule: multiple failed logins → Brute Force (T1110)
    failed_logins = [e for e in events if e.get("action") == "failed_login"]

    if len(failed_logins) >= 3:
        hits.append(
            TechniqueHit(
                technique_id="T1110",
                source="rule",
                confidence=0.8,
                evidence_event_ids=[e["event_id"] for e in failed_logins]
            )
        )

    # Rule: successful login as root/admin → Valid Accounts (T1078)
    privileged_logins = [
        e for e in events
        if e.get("action") == "successful_login"
        and e.get("user") in ("root", "administrator", "admin")
    ]

    if privileged_logins:
        hits.append(
            TechniqueHit(
                technique_id="T1078",
                source="rule",
                confidence=0.7,
                evidence_event_ids=[e["event_id"] for e in privileged_logins]
            )
        )

    return hits
