
---

# Adaptive RAG Pipeline 🦜🔗

An advanced **Retrieval-Augmented Generation (RAG)** system built with LangGraph, featuring:

* ✅ **Adaptive RAG** — Intelligent routing between vectorstore and web search
* ✅ **Self RAG** — Hallucination detection and answer quality verification
* ✅ **Corrective RAG** — Document relevance evaluation before generation
* ✅ **Multi-turn conversations** — Conversation memory support

![Graph](graph.png)

---

## 🚀 Features

### 1️⃣ Intelligent Routing (Adaptive RAG)

The system dynamically decides whether to use the vectorstore or web search based on the user's query.

### 2️⃣ Document Evaluation (Corrective RAG)

Retrieved documents are evaluated for relevance before generating the final answer.

### 3️⃣ Hallucination Detection (Self RAG)

The generated response is checked to ensure it is grounded, relevant, and free from hallucinations.

### 4️⃣ Multi-turn Conversations

Conversation history is maintained using a checkpointer, enabling contextual follow-up questions.

---

## 📋 Prerequisites

* Python 3.13+
* Poetry (for dependency management)
* OpenAI API Key
* Tavily API Key (for web search)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/adaptive-rag-pipeline.git
cd adaptive-rag-pipeline
```

### 2️⃣ Install Dependencies

```bash
poetry install
```

### 3️⃣ Configure Environment Variables

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Then edit the `.env` file:

```bash
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
```

### 4️⃣ Run Ingestion (One-time setup)

Load documents into the vector store:

```bash
poetry run python ingestion.py
```

### 5️⃣ Run the Application

```bash
poetry run python main.py
```

---

## 🏗️ Project Structure

```
adaptive-rag-pipeline/
├── graph/
│   ├── chains/          # LLM chains (grading, generation, etc.)
│   ├── nodes/           # Graph nodes (retrieve, generate, web_search, etc.)
│   ├── state.py         # State definition
│   ├── consts.py        # Constants
│   └── graph.py         # Main graph construction
├── ingestion.py         # Vector store ingestion
├── main.py              # Entry point
├── graph.png            # Graph visualization
├── pyproject.toml       # Poetry configuration
└── README.md            # This file
```

---

## 🎯 Usage

### Basic Example

```python
from graph.graph import app

result = app.invoke({"question": "What is agent memory?"})
print(result["generation"])
```

### Using a ChatSession Wrapper

```python
from graph.graph import app

class ChatSession:
    def __init__(self, thread_id: str):
        self.config = {"configurable": {"thread_id": thread_id}}
    
    def ask(self, question: str):
        result = app.invoke(
            {"question": question},
            config=self.config
        )
        return result["generation"]

# Usage
session = ChatSession(thread_id="user_123")
print(session.ask("What is RAG?"))
print(session.ask("Tell me more"))  # Understands conversation history!
```

---

## 🧪 Running Tests

```bash
poetry run pytest -v
```

---

## 📊 System Workflow

```
User Question
    ↓
Router (Vectorstore or Web Search?)
    ↓
┌───────────┴───────────┐
│                       │
Vectorstore         Web Search
    ↓                   ↓
Grade Documents         │
    ↓                   │
┌───┴───┐               │
│       │               │
Relevant  Not Relevant ─┘
│           │
Generate    Web Search → Generate
    ↓
Check Hallucination
    ↓
Check Relevance to Question
    ↓
Final Answer ✅
```

---

## 🛠️ Technologies Used

* LangChain — Core LLM framework
* LangGraph — Graph-based workflow orchestration
* OpenAI GPT-4 — Language model
* Chroma — Vector database
* Tavily — Web search API
* HuggingFace Embeddings — Text-to-vector embedding model

---

## 📝 License

MIT License — Free to use and modify.

---

## 🤝 Contributing

Pull requests and issues are welcome!

---

## 📧 Contact

* GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
* Email: [your.email@example.com](mailto:your.email@example.com)

---

**Built with ❤️ by [Tina Rostami]**

---

