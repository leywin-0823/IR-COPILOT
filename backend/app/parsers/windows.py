import re
from typing import Dict, Optional
from app.parsers.base import BaseParser


class WindowsSecurityParser(BaseParser):
    """
    Parser for Windows Security Event Logs.
    MVP: Event ID 4625 (Failed Logon).
    """

    def parse(self, raw_log: str) -> Dict[str, Optional[str]]:
        user = None
        source_ip = None
        action = "unknown"

        # Common patterns
        user_match = re.search(r"Account Name:\s+(\S+)", raw_log)
        ip_match = re.search(r"Source Network Address:\s+(\d+\.\d+\.\d+\.\d+)", raw_log)

        if user_match:
            user = user_match.group(1)

        if ip_match:
            source_ip = ip_match.group(1)

        if "4625" in raw_log:
            action = "failed_login"

        return {
            "timestamp": None,   # XML/EVTX parsing later
            "host": None,
            "user": user,
            "action": action,
            "source_ip": source_ip,
            "process": None,
            "raw_log": raw_log,
            "log_type": "windows_security",
        }
