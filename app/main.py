from fastapi import FastAPI
from pydantic import BaseModel
from app.llm_client import call_llm
from app.prompts import CUSTOMER_SUPPORT_PROMPT
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Multi-Task Text Utility")

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/ask")
def ask_question(request: QuestionRequest):
    prompt = f"""
    {CUSTOMER_SUPPORT_PROMPT}

    User question:
    {request.question}
    """

    llm_response = call_llm(prompt, request.question)

    return {
        "answer": llm_response["text"],
        "confidence": llm_response["confidence"],
        "metrics": {
            "latency": llm_response["latency"],
            "tokens": llm_response["tokens_estimated"],
            "estimated_cost": llm_response["estimated_cost"]
        }
    }
