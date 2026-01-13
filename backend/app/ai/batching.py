def batch_events(events: list[dict], batch_size: int = 10):
    for i in range(0, len(events), batch_size):
        yield events[i:i + batch_size]