# Content Moderation System

A Python application that uses OpenAI's language model to perform content moderation on PDF documents.

## Features

- Extracts text from PDF documents
- Processes content through OpenAI's moderation API
- Returns moderation analysis and results

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

3. Place your PDF document in the `data/` directory as `doc.pdf`

## Usage

Run the main script:
```bash
python -m src.main
```

The application will process the PDF document and output moderation results.

## Project Structure

- `src/main.py` - Main entry point
- `src/llm/` - OpenAI integration
- `src/moderation/` - Content moderation logic
- `src/prompt/` - Prompt templates
- `data/` - Document storage

---

### This task took me around 45 - 48 minutes to complete
