import requests
import time
import json
from app.metrics import estimate_tokens, estimate_cost
from app.memory import store_chat, retrieve_similar

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def normalize_llm_text(text: str) -> str:
    """
    Guarantees plain text output.
    Removes markdown, JSON wrappers, and nested answer fields.
    """
    text = text.strip()

    # Remove markdown fences
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    # Try parsing JSON
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict) and "answer" in parsed:
            return parsed["answer"].strip()
    except Exception:
        pass

    # Handle stringified JSON-like output
    if text.startswith("{") and text.endswith("}"):
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict) and "answer" in parsed:
                return parsed["answer"].strip()
        except Exception:
            pass

    return text


def call_llm(prompt: str, question: str):
    # 1️⃣ Check memory first
    cached_answer = retrieve_similar(question)
    if cached_answer:
        tokens = estimate_tokens(cached_answer)
        cost = estimate_cost(tokens)

        return {
            "text": cached_answer,
            "confidence": 0.90,
            "latency": 0.01,
            "tokens_estimated": tokens,
            "estimated_cost": cost,
            "source": "cache"
        }

    # 2️⃣ Call Ollama
    start = time.time()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()
    raw_text = data.get("response", "")
    llm_text = normalize_llm_text(raw_text)

    latency = round(time.time() - start, 2)

    # 3️⃣ Metrics
    tokens = estimate_tokens(llm_text)
    cost = estimate_cost(tokens)

    # 4️⃣ Store clean text only
    store_chat(question, llm_text)

    return {
        "text": llm_text,
        "confidence": 0.75,
        "latency": latency,
        "tokens_estimated": tokens,
        "estimated_cost": cost,
        "source": "ollama"
    }
