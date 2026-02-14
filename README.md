Agentic RAG Assistant
An **Agentic Retrieval-Augmented Generation (RAG)** system that intelligently decides whether to answer a user query directly or retrieve information from uploaded documents before generating a response.
This project demonstrates how modern AI assistants combine **LLMs, vector databases, and intelligent routing agents** to provide accurate, context-aware answers.

 Project Overview
Traditional RAG systems always search documents before answering, even for simple queries.
This project implements an **Agentic RAG pipeline**, where an agent first decides:

*  Answer directly using model knowledge
*  Search uploaded documents and then answer

This improves efficiency, reduces unnecessary retrieval, and mimics real-world AI assistant behavior.


-> Architecture

```
User Query
     │
     ▼
Agent Decision (DIRECT / SEARCH)
     │
 ┌───────────────┬────────────────┐
 │               │
 ▼               ▼
Direct Answer   Vector Search (ChromaDB)
                     │
                     ▼
               Retrieved Context
                     │
                     ▼
                 LLM Response
```

---

-> Features

* Agent-based routing (Direct vs Document search)
* PDF document ingestion
* Semantic search using embeddings
* ChromaDB vector database
* Local LLM support via Ollama
* Flask-based web interface
* Privacy-friendly local execution
* Modular project structure

---

-> Tech Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Backend         | Python, Flask           |
| Agent Logic     | LangChain               |
| Vector Database | ChromaDB                |
| Embeddings      | Sentence Transformers   |
| LLM             | Ollama (Llama3 / Gemma) |
| Frontend        | HTML, CSS               |
| Document Loader | PyPDF                   |

---

-> Project Structure

```
Agentic_RAG/
│
├── app.py
├── requirements.txt
│
├── agent/
│   ├── rag_pipeline.py
│   └── router.py
│
├── vectordb/
│   ├── create_db.py
│   ├── retriever.py
│   └── chroma_db/   (auto-generated)
│
├── data/
│   └── pdfs/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

-> Installation

1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd Agentic_RAG
```

---

2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

4️⃣ Install Ollama

Download from:

https://ollama.com/download

Pull model:

```bash
ollama pull llama3:8b
```

---

5️⃣ Add Documents

Place PDFs inside:

```
data/pdfs/
```

---
6️⃣ Create Vector Database

```bash
python vectordb/create_db.py
```

---
7️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

-> Example Queries

#Direct Answers

```
Hello
What is Artificial Intelligence?
```

#Document-Based Queries

```
Summarize the machine learning PDF
Explain supervised learning from the document
```

---

-> How Agentic RAG Works

1. User sends a query.
2. Agent analyzes intent.
3. If document knowledge is required → retrieval triggered.
4. Relevant chunks are fetched from vector database.
5. LLM generates grounded response.

---

-> Important Notes

* Do NOT upload `vectordb/chroma_db/` to GitHub.
* Always recreate vector DB after cloning:

  ```bash
  python vectordb/create_db.py
  ```
* Requires minimum **8GB RAM** for Llama3:8b.

---

-> Future Improvements

* Streaming responses
* Retrieval validation agent
* Multi-document support
* Query rewriting agent
* Deployment using Docker
* Authentication system

---

## 👨‍💻 Author

**Prakash K**
AI & ML Engineering Student
Project: Agentic RAG Assistant

---

## ⭐ License

This project is for educational and research purposes.
