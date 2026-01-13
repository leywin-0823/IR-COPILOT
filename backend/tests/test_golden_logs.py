from app.parsers.dispatcher import normalize_log

def test_golden_linux_failed_ssh():
    raw = open("tests/golden_logs/linux_failed_ssh.log").read()
    event = normalize_log(raw)

    assert event["log_type"] == "linux_auth"
    assert event["action"] == "failed_login"



def test_golden_windows_failed_login():
    raw = open("tests/golden_logs/windows_failed_login.log").read()
    event = normalize_log(raw)

    assert event["log_type"] == "windows_security"
    assert event["action"] == "failed_login"


def test_golden_sysmon_process():
    raw = open("tests/golden_logs/sysmon_process_create.log").read()
    event = normalize_log(raw)

    assert event["log_type"] == "sysmon"
    assert event["action"] == "process_create"
    assert "powershell.exe" in event["process"]
