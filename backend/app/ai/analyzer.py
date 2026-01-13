from typing import List, Dict

def analyze_events(events: List[Dict]) -> str:
    """
    Deterministic analysis layer.
    This is intentionally simple and explainable.
    LLM integration will wrap this later.
    """

    if not events:
        return "No events provided for analysis."

    actions = {}
    users = set()
    hosts = set()

    for event in events:
        action = event.get("action", "unknown")
        actions[action] = actions.get(action, 0) + 1

        if "user" in event:
            users.add(event["user"])
        if "host" in event:
            hosts.add(event["host"])

    summary_parts = []

    for action, count in actions.items():
        summary_parts.append(f"{count} occurrence(s) of '{action}'")

    summary = ", ".join(summary_parts)

    analysis = (
        f"Observed activity includes {summary}. "
        f"Users involved: {', '.join(users) if users else 'unknown'}. "
        f"Affected hosts: {', '.join(hosts) if hosts else 'unknown'}."
    )

    return analysis
