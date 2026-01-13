from functools import lru_cache

@lru_cache(maxsize=128)
def get_technique_metadata(technique_id: str) -> dict:
    # replace with real metadata source later
    return {
        "id": technique_id,
        "name": "Brute Force",
        "description": "Adversary attempts to guess credentials"
    }
