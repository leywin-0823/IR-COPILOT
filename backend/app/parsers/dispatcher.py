from typing import Dict, Optional

from app.parsers.linux import LinuxAuthParser
from app.parsers.sysmon import SysmonParser
from app.parsers.windows import WindowsSecurityParser


linux_parser = LinuxAuthParser()
sysmon_parser = SysmonParser()
windows_parser = WindowsSecurityParser()


def normalize_log(raw_log: str) -> dict:
    raw = raw_log.lower()

    if "failed password" in raw:
        return LinuxAuthParser().parse(raw_log)

    if "eventid 4625" in raw:
        return WindowsSecurityParser().parse(raw_log)

    if "sysmon" in raw:
        return SysmonParser().parse(raw_log)

    return {
        "log_type": "unknown",
        "timestamp": None,
        "host": None,
        "user": None,
        "process": None,
        "action": "unknown",
        "source": None,
        "raw": raw_log
    }
