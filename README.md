# Research Study Buddy

An intelligent study assistant that leverages embeddings and semantic search to help you understand research materials more effectively.

## 🎯 Overview

Research Study Buddy is a Python-based application designed to help students and researchers quickly extract insights from research papers, PDFs, and other study materials. It uses modern NLP techniques and vector databases to provide intelligent document analysis and Q&A capabilities.

## ✨ Features

- **PDF Document Processing**: Upload and process research papers and study materials
- **Semantic Search**: Find relevant content using natural language queries
- **Intelligent Q&A**: Ask questions about your documents and get accurate answers
- **Vector Embeddings**: Leverage state-of-the-art embeddings for better understanding
- **Persistent Storage**: Store processed documents in Chroma database for quick retrieval
- **Streamlit Interface**: User-friendly web interface for easy interaction

## 📋 Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## 🚀 Installation

1. **Clone or download the project**
   ```bash
   cd Research-Study-Buddy
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Running the Streamlit App
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Main Pipeline
```bash
python main_pipeline.py
```

### Running the Flask App
```bash
python app.py
```

## 📁 Project Structure

```
Research-Study-Buddy/
├── README.md                  # This file
├── requirements.txt           # Python dependencies
├── main_pipeline.py           # Core pipeline logic
├── app.py                     # Flask application
├── streamlit_app.py           # Streamlit web interface
├── test_embeddings.py         # Embedding tests
├── modules/                   # Custom modules and utilities
├── prompts/                   # Prompt templates
├── utils/                     # Utility functions
├── data/                      # Input data directory
├── chroma_db/                 # Vector database storage
├── tests/                     # Test suite
└── venv/                      # Virtual environment (git-ignored)
```

## 🏗️ Architecture Overview

The project architecture is designed as a modular, pipeline-driven study assistant with three main layers:

1. **Input & preprocessing**
   - `utils/pdf_loader.py` loads PDF documents.
   - `utils/text_cleaner.py` and `utils/chunker.py` split and clean text into smaller chunks.
   - `modules/extractor.py` and `modules/indexer.py` prepare data for embedding.

2. **Embedding & storage**
   - `utils/embeddings.py` generates semantic vectors from text chunks.
   - `utils/vector_store.py` and `utils/reset_db.py` manage the Chroma vector database.
   - `chroma_db/` stores the persistent embedding index.

3. **Query & response**
   - `modules/retriever.py` searches the vector store for relevant chunks.
   - `modules/qa.py`, `modules/summarizer.py`, and `modules/table_generator.py` transform retrieved content into answers, summaries, and structured outputs.
   - `streamlit_app.py` and `app.py` provide front-end interfaces for users.

## 🧠 Component Flow

- `main_pipeline.py` orchestrates the end-to-end workflow:
  1. Load documents from `data/`.
  2. Extract and clean text.
  3. Create vector embeddings.
  4. Store vectors in Chroma.
  5. Answer user queries via retrieval and generation.

- `prompts/` stores prompt templates used by the LLM components for consistent task execution.

- `tests/` validates embedding quality, retrieval accuracy, and module behavior.

## 🔧 Configuration

- Create a `.env` file in the project root for environment variables
- Configure API keys and model preferences as needed

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

Test embeddings specifically:
```bash
python test_embeddings.py
```

## 📚 Core Components

### main_pipeline.py
The main pipeline orchestrates document processing, embedding generation, and storage.

### modules/
Contains reusable components for:
- Document processing
- Embedding generation
- Vector database operations
- Query processing

### prompts/
Contains LLM prompt templates for various tasks.

### utils/
Helper functions for file handling, data processing, and common operations.

## 🗄️ Database

The project uses **Chroma** as the vector database for storing and retrieving document embeddings. The database is stored in the `chroma_db/` directory.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📝 License

[Specify your license here]

## 🆘 Troubleshooting

- **Import errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
- **PDF processing issues**: Check that the PDF files are valid and not corrupted
- **Streamlit errors**: Make sure you're running from the project root directory

## 📞 Support

For issues or questions, please open an issue in the repository.

---

**Happy studying! 📚**