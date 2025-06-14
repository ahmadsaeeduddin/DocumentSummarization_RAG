import os
import numpy as np
from .utilis import load_document
from .emb import embed_chunks, create_faiss_index, save_index, save_chunks
from .retrieval import embed_query, retrieve_top_k
from .summarizer import generate_summary

from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize
import faiss
import pickle

def chunk_text(text: str, max_words: int = 100):
    sentences = sent_tokenize(text)
    chunks, chunk = [], []
    word_count = 0
    for sentence in sentences:
        words = sentence.split()
        word_count += len(words)
        chunk.append(sentence)
        if word_count >= max_words:
            chunks.append(' '.join(chunk))
            chunk = []
            word_count = 0
    if chunk:
        chunks.append(' '.join(chunk))
    return chunks

def summarize_pipeline(filepath, query="Summarize this document", k=5):
    # Load and chunk
    print(f"📄 Loading: {filepath}")
    text = load_document(filepath)
    chunks = chunk_text(text)
    print(f"✅ Chunked into {len(chunks)} chunks.")

    # Embedding and indexing
    embeddings = embed_chunks(chunks)
    index = create_faiss_index(np.array(embeddings))
    save_index(index)
    save_chunks(chunks)
    print("✅ Stored FAISS index and chunk data.")

    # Retrieval
    query_embedding = embed_query(query)
    top_indices, distances = retrieve_top_k(query_embedding, index, k)

    top_chunks = [chunks[i] for i in top_indices]
    print("\n🔍 Retrieved Top-K Chunks:")
    for i, chunk in enumerate(top_chunks):
        print(f"\n--- Chunk {i+1} (Distance: {distances[i]:.4f}) ---\n{chunk[:400]}...")
        
    summary = generate_summary(top_chunks)
    print("\n📄 FINAL SUMMARY:\n")
    print(summary)

    return summary

if __name__ == "__main__":
    filepath = os.path.join("data", "d1.txt")
    top_chunks = summarize_pipeline(filepath)
