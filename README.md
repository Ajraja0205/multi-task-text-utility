# 📘 FAQ Support Chatbot – RAG-Style API

This project implements a **Retrieval-Augmented Generation (RAG) style Question Answering API** using **FastAPI** and an open-source language model (`google/flan-t5-base`). It is designed to meet academic and interview-level expectations by returning **structured, explainable responses** instead of vague one-line answers.

---

## 🚀 Features

* ✅ FastAPI-based REST backend
* ✅ RAG-style architecture (Retrieval + Generation)
* ✅ Structured JSON responses
* ✅ Open-source LLM (no OpenAI quota required)
* ✅ Interview / assignment ready

---

## 🧠 What is RAG in this Project?

**Retrieval-Augmented Generation (RAG)** combines:

1. **Retrieval** – Fetching relevant context from a knowledge base (FAQ data)
2. **Generation** – Using an LLM to generate answers grounded in that context

In this project:

* Retrieval is simulated using a keyword-based search over FAQ data
* Generation is handled by `flan-t5-base`

---

## 📂 Project Structure

```text
.
├── main.py        # FastAPI application
├── README.md      # Project documentation
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **FastAPI** – API framework
* **Uvicorn** – ASGI server
* **Transformers (Hugging Face)** – LLM pipeline
* **Flan-T5 Base** – Instruction-tuned language model

---

## 📦 Installation & Setup

### 1️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn transformers torch
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

Server will start at:

👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

Swagger UI:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 🔗 API Endpoints

### ✅ Health Check

**GET /**

Response:

```json
{
  "status": "OK",
  "message": "FAQ RAG Backend Running 🚀"
}
```

---

### 🤖 Ask a Question

**POST /ask**

#### Request Body

```json
{
  "question": "What is RAG architecture?"
}
```

#### Response Body

```json
{
  "user_question": "What is RAG architecture?",
  "system_answer": "RAG architecture stands for Retrieval-Augmented Generation. It retrieves relevant information first and then uses a language model to generate grounded answers.",
  "chunks_related": [
    {
      "content": "RAG stands for Retrieval Augmented Generation. It combines information retrieval with language model generation.",
      "source": "faq",
      "relevance_score": 0.9
    },
    {
      "content": "RAG architecture retrieves relevant documents first and then uses an LLM to generate grounded answers.",
      "source": "faq",
      "relevance_score": 0.9
    }
  ]
}
```

---

## 🧪 Example CURL Command

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What is LLM?"}'
```

---

## 📌 Why This Implementation Is Good

* ❌ Avoids vague LLM-only answers
* ✅ Explains *why* the answer was generated
* ✅ Shows retrieved knowledge chunks
* ✅ Demonstrates understanding of RAG concepts

This makes it suitable for:

* 🎓 Academic assignments
* 💼 Interviews
* 🧪 Proof-of-concept RAG systems

---

## 🔮 Future Enhancements

* Replace keyword retrieval with **FAISS + embeddings**
* Add **CSV / DB logging** (latency, tokens)
* Support **multiple documents**
* Add **confidence scores**

---

## 👨‍💻 Author

**Ansh Jain**

---

✅ *Project is complete, functional, and evaluation-ready.*
