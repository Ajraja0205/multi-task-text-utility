import time
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"

def call_llm(prompt: str):
    start_time = time.time()

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.3, "num_predict": 150}
        },
        timeout=120
    )

    latency = round(time.time() - start_time, 2)

    data = response.json()

    if "response" not in data:
        raise RuntimeError(f"Ollama error: {data}")

    raw_text = data["response"].strip()

    # 🔹 Parse JSON safely
    try:
        llm_json = json.loads(raw_text)
    except json.JSONDecodeError:
        # fallback if model returned extra text
        # strip backticks, newlines, etc
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        llm_json = json.loads(clean_text)

    tokens_estimated = data.get("eval_count", len(llm_json.get("answer", "").split()))
    estimated_cost = round(tokens_estimated * 0.000002, 6)

    # Add latency & tokens into JSON
    llm_json["metrics"] = {
        "latency": latency,
        "tokens": tokens_estimated,
        "estimated_cost": estimated_cost
    }

    return llm_json
