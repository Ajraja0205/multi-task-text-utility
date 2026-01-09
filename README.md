# M1 — FastAPI + Local LLM
Lightweight FastAPI service that demonstrates a local GenAI workflow using Ollama for LLM inference and ChromaDB for semantic memory.

Author: Ansh Jain
Assignment: GenAI – M1
Tech Stack: Python, FastAPI, Ollama, ChromaDB

📌 Overview
This project is part of the M1 (Milestone 1) GenAI Assignment.

The objective is to build a local GenAI-powered text utility that runs entirely offline using:
🦙 Ollama for local LLM inference
⚡ FastAPI for REST APIs
🧠 ChromaDB for semantic memory and caching
🐍 Python for backend logic

The application accepts a user question and returns:
1.A generated answer
2.Confidence score
3.Latency
4.Estimated token usage
5.Estimated cost (0.0 for local LLM)

🎯 Objectives of M1
1.Run an LLM locally (no paid APIs)
2.Build a clean backend service using FastAPI
3.Separate concerns 6.(prompts, LLM client, memory, metrics)
4.Demonstrate prompt-based task handling
5.Track basic performance metrics
Implement semantic memory caching to reduce redundant LLM calls

🏗️ System Architecture
graph TD
    Client[Client / Postman / Swagger UI]

    Client -->|POST /ask| FastAPI[FastAPI App]

    FastAPI --> PromptBuilder[Prompt Builder]
    PromptBuilder --> LLMClient[LLM Client]

    LLMClient --> Memory[ChromaDB<br/>Semantic Memory]

    Memory -->|Cache Hit| FastAPI
    Memory -->|Cache Miss| Ollama[Ollama LLM<br/>phi3 Model]

    Ollama --> LLMClient
    LLMClient --> Metrics[Metrics Engine]
    Metrics --> FastAPI

    FastAPI --> Client

🔁 Request Flow (Sequence)
sequenceDiagram
    participant C as Client
    participant F as FastAPI
    participant M as ChromaDB
    participant L as Ollama LLM

    C->>F: POST /ask (question)
    F->>F: Build system prompt
    F->>M: Query semantic memory

    alt Similar question exists
        M-->>F: Cached answer
        F-->>C: Answer + metrics (cache)
    else No match
        F->>L: Generate response
        L-->>F: Raw LLM output
        F->>F: Normalize output
        F->>M: Store answer
        F-->>C: Answer + metrics (ollama)
    end

🧠 Semantic Memory Decision Flow
flowchart TD
    Q[New Question]
    Q --> Search[Search ChromaDB]
    Search --> Check{Distance < Threshold?}

    Check -->|Yes| Cached[Return cached answer]
    Check -->|No| LLM[Call Ollama]

    LLM --> Clean[Normalize text]
    Clean --> Store[Store in ChromaDB]
    Store --> Return[Return answer]

🧱 Project Structure
multi-task-text-utility/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point
│   ├── llm_client.py      # Ollama LLM + caching logic
│   ├── memory.py          # ChromaDB semantic memory
│   ├── metrics.py         # Latency, token & cost estimation
│   ├── prompts.py         # Prompt templates
│
├── chroma_db/             # Persistent vector storage
├── screenshots/           # API & Swagger screenshots
│
├── requirements.txt
├── .env
├── .env.example
└── README.md

⚙️ Prerequisites

Ensure the following are installed:
Python 3.10+
Ollama
Git (optional)
Postman / Browser

🦙 Ollama Setup (Local LLM)
1️⃣ Verify installation
ollama --version
ollama pull phi3
(Other supported models: llama3, mistral)

2️⃣ Test model
ollama run phi3

🐍 Python Environment Setup
1️⃣ Create virtual environment
python -m venv venv

2️⃣ Activate environment
Windows : venv\Scripts\Activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Running the Application
uvicorn app.main:app --reload

App will be available at: http://127.0.0.1:8000

🌐 API Endpoints
✅ Health Check

GET /
Response: { "status": "ok" }

🤖 Ask Question

POST /ask

Request:
{
  "question": "My internet is not working, what should I do?"
}

Response:
{
  "answer": "You can try restarting your router...",
  "confidence": 0.75,
  "metrics": {
    "latency": 1.23,
    "tokens": 132,
    "estimated_cost": 0.0
  }
}

📊 Metrics Explanation
Latency – Response time (seconds)
Tokens (Estimated) – Approximate token count
Estimated Cost – Always 0.0 (local inference)

🧠 Prompt Design
Prompts are stored in prompts.py: 
CUSTOMER_SUPPORT_PROMPT = """
You are a helpful AI assistant.
Answer clearly in plain English.
Do not return JSON or code blocks.
"""

This ensures:
Prompt reusability
Clean separation of concerns
Easy extension to future tasks

💾 Semantic Memory (ChromaDB)
Answers are stored as vector embeddings
Similar questions are reused automatically
Distance threshold prevents incorrect reuse
Persistent across restarts

This improves:
Latency
Cost efficiency
Answer consistency

📁 Environment Variables

.env.example

LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=phi3
LLM_TIMEOUT=60

🧪 API Documentation (Swagger)

FastAPI auto-docs: http://localhost:8000/docs

🚀 Future Enhancements (M2+)
Multi-task routing (summarization, classification)
Streaming responses
Dockerization
Authentication
RAG with document ingestion
Advanced logging & observability

✅ M1 Checklist

✔ Local LLM via Ollama
✔ FastAPI backend
✔ Prompt separation
✔ Metrics captured
✔ Semantic memory (ChromaDB)
✔ Fully local & offline
✔ Evaluation-ready

👤 Author

Ansh Jain
GenAI – M1 Assignment
Focused on scalable LLM systems & clean backend architecture

📌 Notes
No paid APIs used
Fully local execution
Suitable for offline development & evaluation

✅ M1 Assignment Completed Successfully
✅ Extended with semantic memory and caching