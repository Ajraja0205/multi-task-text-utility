from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import time

# Initialize FastAPI
app = FastAPI(title="FAQ Support Chatbot (RAG-style)")

# Load instruction-tuned model
qa_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

# ----------- Fake FAQ Knowledge Base (RAG source) -----------

FAQ_DATA = [
    {
        "content": "RAG stands for Retrieval Augmented Generation. It combines information retrieval with language model generation.",
        "source": "faq",
    },
    {
        "content": "RAG architecture retrieves relevant documents first and then uses an LLM to generate grounded answers.",
        "source": "faq",
    },
    {
        "content": "FastAPI is a modern Python web framework for building APIs.",
        "source": "faq",
    }
]

# ----------- Models -----------

class QuestionRequest(BaseModel):
    question: str

class Chunk(BaseModel):
    content: str
    source: str
    relevance_score: float

class QuestionResponse(BaseModel):
    user_question: str
    system_answer: str
    chunks_related: list[Chunk]

# ----------- Helper Functions -----------

def retrieve_chunks(question: str):
    """
    Simple keyword-based retrieval (mock RAG).
    """
    results = []

    for item in FAQ_DATA:
        if "rag" in question.lower() and "rag" in item["content"].lower():
            results.append({
                "content": item["content"],
                "source": item["source"],
                "relevance_score": 0.9
            })

    return results[:2]  # top-k

# ----------- Routes -----------

@app.get("/")
def health_check():
    return {"status": "OK", "message": "FAQ RAG Backend Running 🚀"}

@app.post("/ask", response_model=QuestionResponse)
def ask_question(payload: QuestionRequest):
    start_time = time.time()

    retrieved_chunks = retrieve_chunks(payload.question)

    context = "\n".join([c["content"] for c in retrieved_chunks])

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{payload.question}

Answer clearly and completely.
"""

    result = qa_pipeline(prompt, max_length=200, do_sample=False)

    return {
        "user_question": payload.question,
        "system_answer": result[0]["generated_text"],
        "chunks_related": retrieved_chunks
    }
