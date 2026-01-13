from pydantic import BaseModel
from typing import List, Dict, Any

class AIAnalyzeRequest(BaseModel):
    events: List[Dict[str, Any]]
