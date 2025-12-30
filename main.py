from fastapi import FastAPI
from pydantic import BaseModel
import time
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI(title="Multi-Task Text Utility")

# Request body schema
class QuestionRequest(BaseModel):
    question: str

# Response schema (optional but good practice)
class QuestionResponse(BaseModel):
    answer: str
    latency_seconds: float
    tokens_used: int
    estimated_cost_usd: float


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    start_time = time.time()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": request.question}
        ]
    )

    end_time = time.time()

    answer = response.choices[0].message.content
    tokens_used = response.usage.total_tokens

    # Approx cost for gpt-4o-mini (example)
    cost_per_1k_tokens = 0.00015
    estimated_cost = (tokens_used / 1000) * cost_per_1k_tokens

    return {
        "answer": answer,
        "latency_seconds": round(end_time - start_time, 3),
        "tokens_used": tokens_used,
        "estimated_cost_usd": round(estimated_cost, 6)
    }
