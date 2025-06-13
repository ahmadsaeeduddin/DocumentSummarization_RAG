import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os

# Load pre-trained model once
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight but powerful

def embed_chunks(chunks):
    """Convert text chunks to vector embeddings."""
    return model.encode(chunks, show_progress_bar=True)

def create_faiss_index(embeddings):
    """Create a FAISS index from embeddings (for searching later)."""
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)  # L2 distance = Euclidean
    index.add(embeddings)
    return index

def save_index(index, filepath="embedding/faiss_index.index"):
    faiss.write_index(index, filepath)

def save_chunks(chunks, filepath="embedding/chunks.pkl"):
    with open(filepath, 'wb') as f:
        pickle.dump(chunks, f)

def load_index(filepath="embedding/faiss_index.index"):
    return faiss.read_index(filepath)

def load_chunks(filepath="embedding/chunks.pkl"):
    with open(filepath, 'rb') as f:
        return pickle.load(f)
