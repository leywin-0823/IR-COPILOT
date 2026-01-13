import re
from typing import Dict, Optional
from app.parsers.base import BaseParser


class LinuxAuthParser(BaseParser):
    """
    Parser for Linux auth.log entries (SSH-focused for MVP).
    """

    def parse(self, raw_log: str) -> Dict[str, Optional[str]]:
        user = None
        source_ip = None
        action = "unknown"

        # Example:
        # Failed password for invalid user admin from 192.168.1.10 port 22 ssh2
        failed_match = re.search(r"Failed password for (invalid user )?(\w+)", raw_log)
        ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", raw_log)

        if failed_match:
            user = failed_match.group(2)
            action = "failed_login"

        if ip_match:
            source_ip = ip_match.group(1)

        return {
            "timestamp": None,          # auth.log timestamps parsed later
            "host": None,
            "user": user,
            "action": action,
            "source_ip": source_ip,
            "process": "sshd",
            "raw_log": raw_log,
            "log_type": "linux_auth",
        }
