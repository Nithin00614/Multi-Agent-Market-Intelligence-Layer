### 🚀 AI Market Intelligence System

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LLM](https://img.shields.io/badge/LLM-OpenAI-orange)
![LangGraph](https://img.shields.io/badge/LangGraph-MultiAgent-purple)

An LLM-powered multi-agent system that generates structured market intelligence reports by combining real-time data, financial metrics, and retrieval-augmented knowledge.

---

## 🧠 What it does

Given a company name, the system:

- Fetches real-time news
- Retrieves financial metrics
- Augments context using RAG (FAISS)
- Applies LLM reasoning
- Generates:
  - Market summary
  - Risks & opportunities
  - Investment strategy + confidence

---

## ⚙️ Architecture (Simplified)

UI → FastAPI → LangGraph → Agents → LLM → Response

 ➡️ For detailed architecture, design, tradeoffs :
 - Refer to: [system_design.md](system_design.md)

---

## 🧩 Tech Stack

- Backend: FastAPI
- Orchestration: LangGraph
- LLM: Groq (LLaMA3)
- Embeddings: HuggingFace
- Vector DB: FAISS
- Frontend: Streamlit

---

## 📁 Project Structure

app/  
├── agents/  
├── api/  
├── config/  
├── prompts/  
├── schemas/  
├── services/  
├── tools/  
├── workflows/  
└── main.py  
|__
data/  
docker/
system_design.md   

---

## 🚀 Getting Started

1. Clone repo

git clone https://github.com/Nithin00614/Market-Intelligence-Layer

cd Market-intelligence-agent

2. Setup environment

python -m venv venv

Activate:

- Windows → "venv\Scripts\activate"
- Mac/Linux → "source venv/bin/activate"

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Create ".env" file:

- GROQ_API_KEY=your_api_key
- MODEL_NAME=llama3-8b-8192
- NEWS_API_KEY = your_api_key
- FINANCIAL_API_KEY = your_api_key

5. Run backend

uvicorn app.main:app --reload

6. Run UI

streamlit run app.py

---

📤 Example Request

{
  "company": "Apple",
  "question": "Analyze Market Position"
}

---

📈 Example Output

{
  "analysis": {
    "summary": "...",
    "key_risks": [...],
    "opportunities": [...]
  },
  "strategy": {
    "decision": "Hold",
    "confidence": "High"
  }
}

---

⚠️ Limitations

- Relies on external APIs (latency dependent)
- LLM outputs are probabilistic
- FAISS is not distributed (local setup)

---

🎯 Key Highlights

- Multi-agent AI system using LangGraph
- Tool-augmented LLM reasoning
- Retrieval-Augmented Generation (RAG)
- Modular, production-style architecture

---
