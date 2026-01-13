from app.parsers.windows import WindowsSecurityParser

def test_windows_failed_login():
    parser = WindowsSecurityParser()

    raw_log = (
        "EventID 4625: An account failed to log on. "
        "Account Name: admin Source Network Address: 192.168.1.20"
    )

    event = parser.parse(raw_log)

    assert event["log_type"] == "windows_security"
    assert event["action"] == "failed_login"
    assert event["user"] == "admin"
    assert event["source_ip"] == "192.168.1.20"
