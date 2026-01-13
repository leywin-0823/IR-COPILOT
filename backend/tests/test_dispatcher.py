from app.parsers.dispatcher import normalize_log

def test_dispatch_linux_log():
    raw = "Failed password for root from 10.0.0.5 port 22 ssh2"
    event = normalize_log(raw)

    assert event["log_type"] == "linux_auth"
    assert event["action"] == "failed_login"


def test_dispatch_windows_log():
    raw = "Security EventID 4625 Account Name: admin Source Network Address: 10.0.0.9"
    event = normalize_log(raw)

    assert event["log_type"] == "windows_security"


def test_dispatch_sysmon_log():
    raw = "This is a sysmon log"
    event = normalize_log(raw)

    assert event["log_type"] == "sysmon"
    assert event["action"] == "unknown"
