from uuid import uuid4

import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from src.utils.embedding import emb_model


index = faiss.IndexFlatL2(len(emb_model.embed_query("hello world")))


vector_store = FAISS(
    embedding_function=emb_model,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)


def add_to_vector_store(documents):

    uuids = [str(uuid4()) for _ in range(len(documents))]

    vector_store.add_documents(documents=documents, ids=uuids)


def query_vector_store(query):
    results = vector_store.similarity_search_with_score(
        query,
        k=3,
    )
    
    chunks = []
    scores = []
    
    for res, score in results:
        chunks.append(res.page_content)
        scores.append(float(score))
    
    return {"chunks": chunks, "scores": scores}
