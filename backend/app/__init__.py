import json
from pathlib import Path

from app.validation.expectations import EXPECTED_RESULTS
from app.attack.mapper import map_techniques
from app.severity.scorer import calculate_severity

DATASET_DIR = Path("datasets/validation")


def run_validation():
    results = []

    for dataset_file in DATASET_DIR.glob("*.json"):
        name = dataset_file.name

        if name not in EXPECTED_RESULTS:
            raise KeyError(f"No expectations defined for dataset: {name}")

        events = json.loads(dataset_file.read_text())
        expectations = EXPECTED_RESULTS[name]

        # 🔒 HARD TYPE ASSERT (this will catch the bug explicitly)
        if not isinstance(expectations, dict):
            raise TypeError(
                f"Expectations for {name} must be dict, got {type(expectations)}: {expectations}"
            )

        techniques = map_techniques(events)
        severity = calculate_severity(events, techniques)

        expected_techniques = expectations.get("techniques", [])
        min_sev = expectations.get("min_severity")
        max_sev = expectations.get("max_severity")

        detected_ids = {t.technique_id for t in techniques}

        for tid in expected_techniques:
            assert tid in detected_ids, f"{name}: expected technique {tid} not detected"

        if min_sev:
            assert severity.level in (
                min_sev,
                max_sev,
            ), f"{name}: severity {severity.level} outside expected range"

        results.append(
            {
                "dataset": name,
                "techniques": list(detected_ids),
                "severity": severity.level,
            }
        )

    return results
