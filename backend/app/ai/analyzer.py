from app.core.errors import AnalysisError

def analyze_events(events):
    try:
        # existing LLM logic
        return result
    except TimeoutError as e:
        raise RuntimeError("LLM timeout") from e
