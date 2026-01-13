from app.privacy.redaction import redact_event

def test_ip_redaction():
    event = {"source_ip": "10.0.0.5"}
    redacted = redact_event(event)

    assert redacted["source_ip"] == "[REDACTED_IP]"
