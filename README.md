# 📘 M1 Assignment – Multi-Task Text Utility (Local LLM using Ollama)

## 📌 Overview

This project is part of the **M1 (Milestone 1) GenAI Assignment**. The goal is to build a **local GenAI-powered text utility** using:

* **Ollama** for running Large Language Models locally
* **FastAPI** for exposing REST APIs
* **Python** for backend logic

The application exposes an API endpoint that accepts a user question, sends it to a locally running LLM, and returns:

* The generated answer
* Basic metrics such as latency, token estimation, and cost estimation

---

## 🎯 Objectives of M1

* Run an LLM **locally** (no OpenAI / paid APIs)
* Build a clean backend service using FastAPI
* Separate concerns: prompts, LLM client, metrics
* Demonstrate prompt-based task handling
* Track basic performance metrics

---

## 🧱 Project Structure

```
multi-task-text-utility/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── llm_client.py      # Ollama LLM integration
│   ├── prompts.py         # Prompt templates
│   ├── metrics.py         # Latency, token & cost estimation
│   └── __init__.py
│
├── venv/                  # Python virtual environment
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .env (optional)        # Environment variables (if needed)
```

---

## ⚙️ Prerequisites

Make sure the following are installed on your system:

* **Python 3.10+** (recommended: 3.11 or 3.12)
* **Ollama** (installed and added to PATH)
* **Git** (optional)
* **Postman** or browser (for API testing)

---

## 🦙 Ollama Setup (Local LLM)

### 1️⃣ Verify Ollama installation

```bash
ollama --version
```

If not installed, download from:
[https://ollama.com](https://ollama.com)

---

### 2️⃣ Pull a model (example: llama3)

```bash
ollama pull llama3
```

You can also use:

* `mistral`
* `phi3`

---

### 3️⃣ Test model locally

```bash
ollama run llama3
```

If the model responds, Ollama is working correctly.

---

## 🐍 Python Environment Setup

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate virtual environment

**Windows (PowerShell):**

```bash
venv\Scripts\Activate.ps1
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

From the project root directory:

```bash
uvicorn app.main:app --reload
```

Expected output:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 API Endpoints

### ✅ Health Check

**GET** `/`

```
http://localhost:8000/
```

Response:

```json
{
  "status": "ok"
}
```

---

### 🤖 Ask Question (Main Endpoint)

**POST** `/ask`

```
http://localhost:8000/ask
```

#### Headers

```
Content-Type: application/json
```

#### Request Body

```json
{
  "question": "My internet is not working, what should I do?"
}
```

#### Sample Response

```json
{
  "answer": "You can try restarting your router...",
  "metrics": {
    "latency": 1.74,
    "tokens": 128,
    "estimated_cost": 0.0
  }
}
```

---

## 📊 Metrics Explanation

The following metrics are captured:

* **Latency** – Time taken for the LLM to respond (in seconds)
* **Tokens (Estimated)** – Rough token count based on text length
* **Estimated Cost** – Always `0.0` since Ollama runs locally

---

## 🧠 Prompt Design

Prompts are stored in `prompts.py` and injected dynamically.

Example:

```python
CUSTOMER_SUPPORT_PROMPT = """
You are a helpful customer support assistant.
Answer politely and clearly.
"""
```

This ensures:

* Reusability
* Clean separation of logic
* Easy extension for future tasks

---

## 📁 Environment Variables (.env)

For M1, `.env` is **optional**.

If used, it may contain:

```
OLLAMA_MODEL=llama3
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 🧪 API Documentation (Swagger UI)

FastAPI provides automatic API docs:

```
http://localhost:8000/docs
```

This can be used for quick testing and screenshots for submission.

---

## 🚀 Future Enhancements (M2+)

* Multiple task routing (summarization, classification, rewrite)
* Streaming responses
* Authentication
* Dockerization
* Advanced metrics & logging

---

## ✅ M1 Checklist

✔ Local LLM via Ollama
✔ FastAPI backend
✔ Clean project structure
✔ Prompt separation
✔ Metrics captured
✔ Postman & Swagger tested

---

## 👤 Author

**Name:** Ansh Jain
**Assignment:** GenAI – M1
**Tech Stack:** Python, FastAPI, Ollama, LLMs

---

## 📌 Notes

* No paid APIs used
* Entire project runs locally
* Suitable for offline development

---

✅ **M1 Assignment Completed Successfully**
✅ *Project is complete, functional, and evaluation-ready.*
