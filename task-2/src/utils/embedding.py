from langchain_huggingface import HuggingFaceEmbeddings


emb_model = HuggingFaceEmbeddings(model_name='intfloat/e5-small-v2')

def embed_query(query):
    embedding = emb_model.embed_query(query)

    return embedding
