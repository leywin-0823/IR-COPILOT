from app.parsers.sysmon import SysmonParser

def test_sysmon_process_create():
    parser = SysmonParser()

    raw_log = (
        "Sysmon EventID 1: Process Create "
        "Image: C:\\Windows\\System32\\cmd.exe ParentImage: explorer.exe"
    )

    event = parser.parse(raw_log)

    assert event["log_type"] == "sysmon"
    assert event["action"] == "process_create"
    assert "cmd.exe" in event["process"]
