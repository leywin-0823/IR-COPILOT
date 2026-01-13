class BaseParser:
    log_type = "unknown"

    def normalize(self, raw_log: str, event: dict) -> dict:
        return {
            "log_type": self.log_type,
            "timestamp": event.get("timestamp"),
            "host": event.get("host"),
            "user": event.get("user"),
            "process": event.get("process"),
            "action": event.get("action", "unknown"),
            "source": event.get("source"),
            "raw": raw_log
        }
