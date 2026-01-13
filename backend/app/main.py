from fastapi import FastAPI, HTTPException
from app.api.ai_routes import router as ai_router
from app.schemas import LogIngestRequest, NormalizedEvent
from app.parsers.dispatcher import normalize_log

app = FastAPI(title="IR Copilot API", version="0.1")
app.include_router(ai_router)

@app.get("/")
def health():
    return {"status": "ok", "service": "ir-copilot"}

@app.post("/ingest", response_model=NormalizedEvent)
def ingest_log(payload: LogIngestRequest):
    raw_log = payload.raw_log.strip()

    if not raw_log:
        raise HTTPException(status_code=400, detail="Empty log input")

    try:
        event = normalize_log(raw_log)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return event
