import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def call_llm(prompt: str):
    start_time = time.time()

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    latency = time.time() - start_time

    result = response.json()

    return {
        "text": result.get("response", ""),
        "latency": round(latency, 3),
        "tokens_estimated": len(result.get("response", "").split()),
        "estimated_cost": 0.0  # Local model
    }
