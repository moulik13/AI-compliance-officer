# 🛡️ AI Compliance Officer

An end-to-end, multi-agent AI system that analyzes documents, meeting transcripts, and policy files to detect potential policy violations and legal risks — powered by LLMs, CrewAI, and modern DevOps tools.

---

## 🧠 Project Overview

**AI Compliance Officer** is a production-ready tool that uses a multi-agent architecture to:
- Analyze uploaded company documents (PDFs, transcripts, etc.)
- Detect internal policy violations (e.g., data leaks, HR misconduct)
- Provide legal risk assessments
- Generate actionable suggestions (e.g., alert HR, revise language)

This project is built to demonstrate how intelligent agent collaboration, local LLMs, and scalable infrastructure can be combined to build secure, useful, and auditable AI workflows.

---

## 🧩 Tech Stack

| Layer | Tools Used |
|-------|-------------|
| Backend | FastAPI, Python |
| Multi-Agent System | CrewAI |
| NLP & LLMs | Hugging Face Transformers, Ollama (Whisper, LLaMA3, Mistral) |
| Frontend (Optional) | Streamlit / React |
| Containerization | Docker |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Others | pdfminer.six, langchain, pydantic, logging, etc. |

---

## ⚙️ Features

- ✅ Upload and parse PDFs / transcripts
- ✅ Summarize documents using LLMs
- ✅ Check for compliance violations (e.g., GDPR, Code of Conduct)
- ✅ Run agents that analyze and collaborate on legal risk assessment
- ✅ Generate recommended next actions (e.g., escalate, alert team)
- ✅ Modular and testable agent architecture using CrewAI
- ✅ Locally run models via Ollama (no vendor lock-in)
- ✅ Deployable with Docker and Kubernetes

---

## 📁 Project Structure
ai-compliance-officer/
- ├── api/ # FastAPI backend
- ├── agents/ # CrewAI agent logic
- ├── models/ # LLM wrappers for summarization, classification
- ├── utils/ # Parsers, templates, logger
- ├── test_data/ # Sample PDFs, transcripts
- ├── frontend/ # Streamlit/React UI (optional)
- ├── Dockerfile
- ├── docker-compose.yml
- ├── k8s/ # Kubernetes deployment manifests
- ├── requirements.txt
- └── README.md
