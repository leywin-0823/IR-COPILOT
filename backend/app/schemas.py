from pydantic import BaseModel, Field

class LogIngestRequest(BaseModel):
    raw_log: str = Field(..., min_length=5, description="Raw log text")

class NormalizedEvent(BaseModel):
    log_type: str
    timestamp: str | None = None
    host: str | None = None
    user: str | None = None
    process: str | None = None
    action: str | None = None
    source: str | None = None
