# 🧠 AI Workflow Orchestrator

An AI-powered workflow automation system built using **LangChain**, **Hugging Face Transformers**, and **Streamlit**.

### 🎯 Features (MVP)
- Fetches latest AI news
- Summarizes content using open models
- Generates LinkedIn-style professional posts
- Fully free and open-source deployment (Streamlit Cloud)

---

### ⚙️ Tech Stack
| Layer | Technology |
|-------|-------------|
| Frontend | Streamlit |
| Backend | LangChain |
| LLM | Hugging Face (Flan-T5 / BART) |
| Data Source | NewsAPI / Web Scraper |
| Hosting | Streamlit Cloud |

---

### 🏗️ Folder Structure
    src/
├── agents/
├── tools/
├── utils/
└── main.py
app.py

### 🧩 Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Copy code
