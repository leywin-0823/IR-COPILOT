import re
from app.parsers.base import BaseParser

class SysmonParser(BaseParser):
    log_type = "sysmon"

    def parse(self, raw_log: str) -> dict:
        event = {
            "action": "unknown",
            "process": None
        }

        if "EventID 1" in raw_log:
            event["action"] = "process_create"

            image_match = re.search(r"Image:\s+([^\s]+)", raw_log)
            if image_match:
                event["process"] = image_match.group(1)

        return self.normalize(raw_log, event)
