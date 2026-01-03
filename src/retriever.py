# Load the Pre-built Vector Store

from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Load embeddings model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector store
with open('vector_store/faiss_index.pkl', 'rb') as f:
    faiss_index = pickle.load(f)

# Load metadata (text chunks) corresponding to embeddings
with open('vector_store/metadata.pkl', 'rb') as f:
    metadata = pickle.load(f)

# Implement the Retriever
# Create a function that embeds the question and retrieves top-k similar
# src/retriever.py

def retrieve_chunks(question, k=5):
    # Embed the question
    question_embedding = embed_model.encode([question])
    
    # FAISS similarity search
    distances, indices = faiss_index.search(question_embedding, k)
    
    # Fetch corresponding text chunks
    retrieved_chunks = [metadata[idx] for idx in indices[0]]
    return retrieved_chunks
