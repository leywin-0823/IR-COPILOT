import requests
from app.core.state import PRIVACY_CONFIG

def call_cloud_llm(prompt: str) -> str:
    if not PRIVACY_CONFIG.allow_cloud_llm:
        raise RuntimeError(
            "Cloud LLM access is disabled by privacy configuration"
        )

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def call_ollama(prompt: str) -> str:
    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    },
    timeout=60
)

    response.raise_for_status()
    return response.json()["response"]
