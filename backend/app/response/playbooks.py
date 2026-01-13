BRUTE_FORCE_PLAYBOOK = {
    "investigation": [
        {
            "title": "Review authentication logs",
            "description": "Review recent authentication attempts for the affected account to determine frequency, source IPs, and success/failure patterns.",
        },
        {
            "title": "Check for successful logins",
            "description": "Determine whether any failed attempts were followed by a successful login from the same source.",
        },
    ],
    "containment": [
        {
            "title": "Temporarily lock affected account",
            "description": "Lock or restrict the affected account to prevent further unauthorized attempts.",
        },
        {
            "title": "Block source IP",
            "description": "If malicious, block the source IP address at the firewall or network edge.",
        },
    ],
    "recovery": [
        {
            "title": "Reset credentials",
            "description": "Reset passwords or rotate credentials associated with the affected account.",
        },
    ],
}
