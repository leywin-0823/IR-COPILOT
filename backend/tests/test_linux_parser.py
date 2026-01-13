from app.parsers.linux import LinuxAuthParser

def test_failed_ssh_login():
    parser = LinuxAuthParser()

    raw_log = (
        "Jan 10 10:12:33 server sshd[1234]: "
        "Failed password for invalid user admin from 192.168.1.10 port 22 ssh2"
    )

    event = parser.parse(raw_log)

    assert event["log_type"] == "linux_auth"
    assert event["action"] == "failed_login"
    assert event["user"] == "admin"
    assert event["source_ip"] == "192.168.1.10"
    assert event["process"] == "sshd"
