# 📚 LangChain RAG Chatbot with ChromaDB and Flask

A lightweight **Retrieval-Augmented Generation (RAG)** chatbot that combines the power of local embeddings, efficient vector search, and an interactive chat UI.

---

## ✨ Overview

This project is a fully functional chatbot built with:

- 🧠 **LangChain** – For chaining LLMs with tools like retrievers and memory
- 📦 **ChromaDB** – As the vector store for fast similarity search
- 💬 **HuggingFace Embeddings** – Local model (`all-MiniLM-L6-v2`) for privacy and no external API dependency
- 🌐 **Flask** – Web interface with a responsive, minimalistic chat-style UI
- ⚙️ **Optional** – Support for OpenAI API for LLM responses (can be replaced)

---

## 🖼️ Demo Screenshot

![Chatbot Screenshot](https://github.com/user-attachments/assets/c4e47f0b-ab58-4ba4-aaaf-d8da1a8af285)

---

## 🚀 Features

- ✅ Local embedding using HuggingFace (`sentence-transformers`)
- 🧠 RAG pipeline with document retrieval and response generation
- 💬 Chat UI with session-based conversation memory
- 📱 Clean, mobile-friendly frontend using Flask + HTML/CSS
- 🔄 Easy to extend with new documents, embeddings, or LLMs

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/arryc2021/Metadata-science-platform.git
cd Metadata-science-platform
2. Install Dependencies
If requirements.txt is available:

bash
Copy
Edit
pip install -r requirements.txt
Or manually install the key dependencies:

bash
Copy
Edit
pip install flask flask-session langchain chromadb sentence-transformers openai
🧠 (Optional) Set OpenAI API Key
If you'd like to use OpenAI's LLMs instead of local ones:
export OPENAI_API_KEY=your-key-here
# On Windows:
# set OPENAI_API_KEY=your-key
📄 Prepare Your Data
Add your knowledge base as plain text in a file named data.txt.

Example:
# Download or create your dataset
wget https://example.com/data.txt
Make sure the file is named data.txt and placed in the root directory.

🔄 Ingest Data into ChromaDB
Run the data ingestion script:
python ingest.py
This will:

Load the data.txt file

Split the content into manageable chunks

Generate local embeddings using a HuggingFace model

Store embeddings in chroma_db/

💬 Run the Flask App
To start the chatbot:
python app.py
Then open your browser and go to:

http://localhost:5000
🧪 Example Questions
Once the chatbot is running, try asking:

"What is leadership?"

"Summarize chapter 4."

"Give me a quote about leadership."

🗂️ Project Structure
├── app.py              # Flask app with chat session
├── agent.py            # RAG logic: retrieval and LLM response
├── ingest.py           # Script for document ingestion and embedding
├── data.txt            # Plain text knowledge base
├── templates/
│   └── index.html      # Frontend chat UI
├── chroma_db/          # Persisted vector database
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🎯 Project Objective
The goal of this project is to demonstrate how to build a fully local, customizable RAG chatbot using modern open-source tools. It’s ideal for:

Educational purposes in NLP/LLM pipelines

Building Q&A bots from custom knowledge sources

Rapid prototyping for AI assistants without cloud dependency

🤝 Contributing
Pull requests, issues, and feedback are welcome!

If you'd like to contribute:

Fork the repo

Create a new branch (git checkout -b feature-name)

Commit your changes

Push to your fork

Open a pull request
📄 License
This project is licensed under the MIT License – see the LICENSE file for details.


Let me know if you'd like to also include:

- Deployment instructions (Docker, Heroku, etc.)
- Local vs OpenAI toggle instructions
- Extended UI customization options
- Test cases or CI setup

I can help add those as well.


