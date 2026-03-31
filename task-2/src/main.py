import json
from src.utils.extract_text import read_doc
from src.utils.chunking import chunk_doc
from src.utils.vectore_store import add_to_vector_store, query_vector_store


raw_text = read_doc("./data/doc.pdf")
docs = chunk_doc(raw_text)
add_to_vector_store(docs)


query = "How to install Docling in python?"

result = query_vector_store(query)
print(json.dumps(result, indent=2))
