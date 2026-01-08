from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_client import call_llm
from app.prompts import CUSTOMER_SUPPORT_PROMPT

# ✅ Create app FIRST
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
    llm_response = call_llm(prompt)
    return llm_response
