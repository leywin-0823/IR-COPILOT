import json
from pathlib import Path

from app.attack.mapper import map_techniques
from app.severity.scorer import calculate_severity

DATASET_DIR = Path("datasets/validation")

EXPECTED_RESULTS = {
    "brute_force.json": {
        "techniques": ["T1110"],
        "min_severity": "high",
        "should_alert": True,
    },
    "lateral_movement.json": {
        "techniques": ["T1021"],
        "min_severity": "high",
        "should_alert": True,
    },
    "persistence_schtasks.json": {
        "techniques": ["T1053"],
        "min_severity": "high",
        "should_alert": True,
    },
    "suspicious_powershell.json": {
        "techniques": ["T1059"],
        "min_severity": "medium",
        "should_alert": True,
    },
    "benign_login.json": {
        "techniques": [],
        "min_severity": "low",
        "should_alert": False,
    },
}

SEVERITY_ORDER = ["low", "medium", "high", "critical"]


def run_validation():
    print(">>> run_validation() CALLED <<<")

    results = []

    for dataset_file in DATASET_DIR.glob("*.json"):
        name = dataset_file.name
        passed = True
        errors = []

        if name not in EXPECTED_RESULTS:
            raise KeyError(f"No expectations defined for dataset: {name}")

        dataset = json.loads(dataset_file.read_text())

        if "events" not in dataset:
            raise ValueError(f"{name} missing 'events' key")

        events = dataset["events"]
        expectations = EXPECTED_RESULTS[name]

        try:
            techniques = map_techniques(events)
            severity = calculate_severity(events, techniques)

            detected_ids = {t.technique_id for t in techniques}

            # Technique checks
            for tid in expectations["techniques"]:
                if tid not in detected_ids:
                    passed = False
                    errors.append(
                        f"Expected technique {tid} not detected "
                        f"(detected={detected_ids})"
                    )

            # Severity check
            expected_idx = SEVERITY_ORDER.index(expectations["min_severity"])
            actual_idx = SEVERITY_ORDER.index(severity.level)

            if actual_idx < expected_idx:
                passed = False
                errors.append(
                    f"Severity too low: expected >= {expectations['min_severity']}, "
                    f"got {severity.level}"
                )

        except Exception as e:
            passed = False
            errors.append(str(e))

        results.append(
            {
                "dataset": name,
                "passed": passed,               # ✅ ALWAYS PRESENT
                "severity": severity.level if passed else None,
                "detected_techniques": list(detected_ids) if passed else [],
                "errors": errors,
            }
        )

    return results
