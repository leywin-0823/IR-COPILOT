from fastapi import APIRouter, HTTPException
from app.models.ingest import IngestRequest
from app.parsers.dispatcher import normalize_log

router = APIRouter()

@router.post("/ingest")
def ingest_logs(payload: IngestRequest):
    try:
        event = normalize_log(payload.logs)
        return {
            "normalized_event": event
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
