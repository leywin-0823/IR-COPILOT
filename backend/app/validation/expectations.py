EXPECTED_RESULTS = {
    "brute_force.json": {
        "techniques": ["T1110"],
        "min_severity": "high",
        "max_severity": "critical",
    },
    "lateral_movement.json": {
        "techniques": ["T1021"],
        "min_severity": "high",
        "max_severity": "critical",
    },
    "persistence_schtasks.json": {
        "techniques": ["T1053"],
        "min_severity": "medium",
        "max_severity": "high",
    },
    "suspicious_powershell.json": {
        "techniques": ["T1059"],
        "min_severity": "medium",
        "max_severity": "high",
    },
    "benign_login.json": {
        "techniques": [],
        "min_severity": "low",
        "max_severity": "low",
    },
}
