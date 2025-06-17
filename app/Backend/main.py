import os
import numpy as np
from .utilis import load_document
from .emb import embed_chunks, create_faiss_index, save_index, save_chunks
from .retrieval import embed_query, retrieve_top_k
from .summarizer import generate_summary
from bert_score import score

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

def testing(pred_summary):
    ref_summary = "Mentally ill inmates in Miami are housed on the 'forgotten floor' Judge Steven Leifman says most are there as a result of 'avoidable felonies' While CNN tours facility, patient shouts: 'I am the son of the president' Leifman says the system is unjust and he's fighting for change ."
    P, R, F1 = score([pred_summary], [ref_summary], lang='en', verbose=True)
    print(f"BERTScore F1: {F1[0].item():.4f}")

def summarize_pipeline(filepath, k=3):
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
    query="Summarize this document"
    query_embedding = embed_query(query)
    top_indices, distances = retrieve_top_k(query_embedding, index, k)

    top_chunks = [chunks[i] for i in top_indices]
    print("\n🔍 Retrieved Top-K Chunks:")
    for i, chunk in enumerate(top_chunks):
        print(f"\n--- Chunk {i+1} (Distance: {distances[i]:.4f}) ---\n{chunk[:400]}...")
    
    #summary generation
    summary = generate_summary(top_chunks)
    print("\n📄 FINAL SUMMARY GENERATED ---\n")
    
    testing(summary)
    # print(summary)

    return summary

# if __name__ == "__main__":
#     filepath = os.path.join("data", "d1.txt")
#     top_chunks = summarize_pipeline(filepath)
