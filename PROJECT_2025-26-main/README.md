# RAG App for Legal Consultancy

![Legal RAG App](https://img.shields.io/badge/Legal-RAG-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red)
![LangChain](https://img.shields.io/badge/LangChain-0.1.17-orange)

## 📋 Overview

The **RAG App for Legal Consultancy** is an intelligent question-answering application built using **Retrieval-Augmented Generation (RAG)** techniques. It allows users to query large legal documents, such as Indian laws, and receive precise, context-based answers. The app combines **document embeddings**, **vector search**, and a **large language model (LLM)** to deliver accurate and detailed legal information efficiently.

---

## ✨ Features

- **📄 Query large legal documents:** Works with PDFs up to several hundred pages
- **🔍 Full-document retrieval:** Retrieves context from any part of the document, including beginning, middle, and end
- **💡 Detailed answers:** Uses multiple document chunks to provide comprehensive responses
- **💬 Chat-style interface:** Simple and interactive UI for asking questions
- **🔎 Document similarity search:** View which sections of the document contributed to the answer
- **⚡ Fast response time:** Optimized vector search for quick retrieval
- **🔄 Session management:** Maintains conversation history during the session

---

## 🏗️ Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│   User      │────▶│   Streamlit  │────▶│    Groq LLM  │
│   Question  │     │    Interface │     │   (Gemma2)   │
└─────────────┘     └──────────────┘     └──────────────┘
                            │                     ▲
                            ▼                     │
                    ┌──────────────┐     ┌──────────────┐
                    │    FAISS     │────▶│  Retrieved   │
                    │ Vector Store │     │   Context    │
                    └──────────────┘     └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │  Legal PDF   │
                    │  Document    │
                    └──────────────┘
```

---

## 🔧 How It Works

### 1. **Document Loading**
   - Reads PDF documents using `PyPDFLoader`
   - Supports various legal document formats

### 2. **Text Splitting**
   - Splits document into overlapping chunks using `RecursiveCharacterTextSplitter`
   - **Chunk size:** 1000 characters
   - **Overlap:** 200 characters (ensures context continuity between chunks)

### 3. **Embedding Creation**
   - Converts each chunk into vector embeddings using `HuggingFaceEmbeddings` (all-MiniLM-L6-v2 model)
   - Stores embeddings in a **FAISS vector database** for similarity search
   - Persists index locally for faster subsequent loads

### 4. **Retrieval and Generation**
   - Fetches top 5 relevant chunks when a user asks a question
   - Passes chunks to LLM (`ChatGroq Gemma2-9b-It`) via custom prompt template
   - LLM generates detailed, context-aware answers

### 5. **Result Display**
   - Displays the generated answer in chat format
   - Optionally shows the **document chunks** used to generate the answer (expandable section)
   - Maintains conversation history

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.10+** | Core programming language |
| **Streamlit** | Interactive web interface |
| **LangChain** | RAG and LLM orchestration |
| **FAISS** | Vector database for document retrieval |
| **HuggingFace Embeddings** | Converts text chunks into embeddings |
| **ChatGroq (Gemma2-9b-It)** | Large language model for generating answers |
| **PyPDF** | PDF document loading and parsing |
| **Sentence-Transformers** | Embedding model backend |

---

## 📁 Project Structure

```
PROJECT_2025-26-main/
├── src/
│   ├── APP.py                 # Main Streamlit application
│   ├── legal_document.pdf      # Your legal PDF document
│   ├── faiss_index/            # Vector store directory (created after first run)
│   └── .streamlit/
│       └── secrets.toml        # API keys (not committed to GitHub)
├── requirements.txt            # Project dependencies
├── README.md                   # This file
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Groq API key (get it from [Groq Console](https://console.groq.com))

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/legal-rag-chatbot.git
cd legal-rag-chatbot
```

### Step 2: Create Virtual Environment
```bash
# Using conda (recommended)
conda create -n legal-rag python=3.10
conda activate legal-rag

# OR using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Key
Create `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your-groq-api-key-here"
```

### Step 5: Add Your Legal Document
Place your legal PDF document in the `src/` folder and update the filename in `APP.py` if needed.

### Step 6: Run the Application
```bash
cd src
streamlit run APP.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🎯 Usage Guide

1. **First Run:** The app will process your PDF, create embeddings, and build the FAISS index (may take 1-2 minutes)
2. **Ask Questions:** Type your legal question in the chat input
3. **Get Answers:** The AI will respond with context-based information from your document
4. **View Sources:** Click on "View Source Chunks" to see which document sections were used
5. **Continue Conversation:** Ask follow-up questions within the same session

### Example Questions:
- "What are the essential elements of a valid contract?"
- "Explain the concept of fundamental rights"
- "What is the procedure for filing an FIR?"
- "What are the penalties for breach of contract?"
- "Define defamation under Indian law"

---

## 🌐 Deployment

### Deploy on Streamlit Cloud (Free)

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to `src/APP.py`
5. Add your `GROQ_API_KEY` in **Settings → Secrets**
6. Click **Deploy**

Your app will be live at `https://your-app-name.streamlit.app` 🎉

### Alternative Deployment Options
- **Hugging Face Spaces** (free, GPU optional)
- **Render** (free tier available)
- **Google Cloud Run** (pay-as-you-go)

---

## ⚙️ Configuration

You can modify these parameters in `APP.py`:

| Parameter | Current Value | Description |
|-----------|--------------|-------------|
| Chunk Size | 1000 | Size of text chunks for embedding |
| Chunk Overlap | 200 | Overlap between consecutive chunks |
| Top K Results | 5 | Number of chunks to retrieve |
| Model | Gemma2-9b-It | Groq LLM model |
| Embedding Model | all-MiniLM-L6-v2 | HuggingFace embedding model |

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `No module named 'pypdf'` | Run `pip install pypdf` |
| FAISS index loading error | Delete the `faiss_index/` folder and restart |
| API key error | Check `.streamlit/secrets.toml` file |
| Slow first response | Normal due to model loading |
| Memory issues | Reduce chunk size or document size |

---

## 📝 Requirements

```
langchain==0.1.17
langchain-community==0.0.38
langchain-huggingface==0.0.3
langchain-core==0.1.52
streamlit==1.54.0
groq==0.37.1
pypdf==5.4.0
sentence-transformers==5.2.3
faiss-cpu==1.13.2
python-dotenv==1.2.2
numpy==1.26.4
pydantic==2.12.5
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

**Developed by:**  
**Nirabhay Singh Rathod, Aman Bansal, Ahmad Raja Khan**

📧 **Email:** ahmadrajak0011@gmail

🔗 **GitHub:** [Your GitHub Profile](https://github.com/00Raja11)

🌐 **Project Link:** [https://github.com/yourusername/legal-rag-chatbot](https://github.com/yourusername/legal-rag-chatbot)

---

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the amazing RAG framework
- [Groq](https://groq.com/) for providing fast LLM inference
- [Streamlit](https://streamlit.io/) for the easy-to-use web framework
- [HuggingFace](https://huggingface.co/) for embedding models

---

## 📊 Future Enhancements

- [ ] Multi-document support
- [ ] User authentication
- [ ] Chat history persistence
- [ ] Document upload via UI
- [ ] Multiple language support
- [ ] Citation linking to specific pages
- [ ] Export conversations as PDF

---

<div align="center">
  
**Made with ❤️ for Legal Tech**

⭐ Star this repo if you found it helpful!

</div>
```