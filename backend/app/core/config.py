from pydantic import BaseModel

class PrivacyConfig(BaseModel):
        allow_cloud_llm: bool = False
        redact_pii: bool = True
        persist_logs: bool = False