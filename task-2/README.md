# Document Q&A System

A Python application that enables question-answering on PDF documents using vector embeddings and similarity search.

## Features

- Extracts text from PDF documents
- Chunks documents for optimal processing
- Creates vector embeddings for semantic search
- Enables natural language queries on document content

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place your PDF document in the `data/` directory as `doc.pdf`

## Usage

Run the main script:
```bash
python -m src.main
```

The application will:
1. Process the PDF document
2. Create embeddings and store in vector database
3. Answer the sample query: "How to install Docling in python?"
4. Return relevant document chunks

## Project Structure

- `src/main.py` - Main entry point
- `src/utils/` - Utility functions for text extraction, chunking, and vector operations
- `data/` - Document storage

## Customization

Modify the query in `src/main.py` to ask different questions about your document content.
