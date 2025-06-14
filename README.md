# 📄 Document Summarization using Retrieval-Augmented Generation (RAG)

Summarization system combines retrieval-based context selection with large language model (LLM) generation. The system accepts a long document and generate a concise, coherent summary using semantic chunking and RAG.

A complete RAG-based document summarizer that supports PDF, TXT, and MD formats using:
- Semantic chunking
- FAISS vector search
- OpenAI GPT-3.5 summarization
- Flask frontend for file upload and result viewing

---

## 🗂️ Project Structure

```
DOCUMENT-SUMMARIZATION(RAG)/
│
├── app/
│   ├── app.py                # Flask backend
│   ├── Backend/              # Optional backend utils
│   ├── static/
│   │   ├── script.js         # JavaScript functionality
│   │   └── styles.css        # Styling for frontend
│   ├── Summaries/            # Generated summaries (if saved)
│   └── index.html            # Upload and result UI
│
├── Data/                     # Input files uploaded
├── embedding/                # FAISS index and embeddings
├── env/                      # Environment-related files
├── .env                      # Your OpenAI API key (not shared)
├── nltk-download.py          # For downloading NLTK 'punkt'
├── requirements.txt          # Python dependencies
├── README.md                 # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/document-summarizer.git
cd document-summarizer
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Punkt (Run Once)

```bash
python nltk-download.py
```

### 5. Add OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 6. Run the App

```bash
cd app
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🧪 Usage Guide

- Upload a `.pdf`, `.txt`, or `.md` document
- The system:
  1. Loads and chunks the document
  2. Embeds chunks via SentenceTransformers
  3. Uses FAISS to retrieve relevant parts
  4. Summarizes the result using GPT-3.5
- Final summary is shown on screen

---

## ❗ Troubleshooting

| Problem | Solution |
|--------|----------|
| `nltk.punkt not found` | Run `python nltk-download.py` |
| `No module named dotenv` | Run `pip install python-dotenv` |
| `OpenAI Authentication Error` | Check your `.env` key format |
| Flask not starting | Ensure `app.py` is run from inside the `/app` directory |
| No summary output | Check if FAISS index was created and query was valid |

---

## 📌 Notes

- The app is modular. You can reuse `main.py` or split the backend from the Flask frontend easily.
- You can upgrade to GPT-4 by changing the model name in `summarizer.py`.

---

## 🧠 Credits

- FAISS by Facebook AI
- SentenceTransformers by UKPLab
- GPT-3.5 via OpenAI API