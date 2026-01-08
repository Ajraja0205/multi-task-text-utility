import time

def start_timer():
    return time.time()

def end_timer(start_time: float) -> float:
    return round(time.time() - start_time, 3)

def estimate_tokens(text: str) -> int:
    # Simple heuristic: 1 token ≈ 0.75 words
    words = len(text.split())
    return int(words / 0.75)

def estimate_cost(tokens: int) -> float:
    # Local Ollama = free
    return 0.0
