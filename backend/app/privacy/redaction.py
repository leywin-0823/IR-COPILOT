import re

PII_PATTERNS = [
    (re.compile(r"\b\d{1,3}(\.\d{1,3}){3}\b"), "[REDACTED_IP]"),
    (re.compile(r"\broot\b", re.IGNORECASE), "[REDACTED_USER]"),
]

def redact_event(event: dict) -> dict:
    redacted = {}

    for k, v in event.items():
        if isinstance(v, str):
            for pattern, replacement in PII_PATTERNS:
                v = pattern.sub(replacement, v)
        redacted[k] = v

    return redacted
