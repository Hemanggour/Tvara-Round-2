from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50)


def chunk_doc(raw_text):
    docs = []

    split_text = text_splitter.split_text(raw_text)

    for text in split_text:
        docs.append(Document(text))

    return docs
