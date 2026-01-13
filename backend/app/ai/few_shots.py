FEW_SHOT_EXAMPLE = """
EXAMPLE (DO NOT ANALYZE):

Input events:
[
  {
    "event_id": "example-001",
    "timestamp": "2026-01-01T10:00:00Z",
    "action": "failed_login",
    "user": "admin",
    "source_ip": "192.168.1.50"
  }
]

Correct output:
{
  "summary": {
    "title": "Failed administrative login attempt",
    "narrative": "A failed login attempt was recorded for the administrative account from an external IP address. This may indicate an attempt to guess credentials or probe access controls."
  },
  "analysis": {
    "what_happened": "An authentication attempt for the admin account failed.",
    "why_it_matters": "Repeated failed logins against privileged accounts can indicate brute-force or reconnaissance activity.",
    "attack_stage": "credential_access"
  },
  "evidence": [
    {
      "event_id": "example-001",
      "timestamp": "2026-01-01T10:00:00Z",
      "field": "action",
      "value": "failed_login"
    },
    {
      "event_id": "example-001",
      "timestamp": "2026-01-01T10:00:00Z",
      "field": "source_ip",
      "value": "192.168.1.50"
    }
  ],
  "confidence": {
    "level": "medium",
    "reasoning": "This is a single failed attempt without follow-on activity, but it targets a privileged account."
  }
}
END EXAMPLE
"""
