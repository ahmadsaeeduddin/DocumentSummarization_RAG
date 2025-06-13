import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import pickle

def load_index(index_path="embeddings/faiss_index.index"):
    return faiss.read_index(index_path)

def load_chunks(chunk_path="embeddings/chunks.pkl"):
    with open(chunk_path, 'rb') as f:
        return pickle.load(f)

def embed_query(query: str, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    return model.encode([query])

def retrieve_top_k(query_embedding, index, k=5):
    D, I = index.search(query_embedding, k)
    return I[0], D[0]  # I = indices, D = distances
