# src/retriever.py

import chromadb
from chromadb.config import Settings

PERSIST_DIR = "vector_store"
COLLECTION_NAME = "complaints"

client = chromadb.Client(
    Settings(
        persist_directory=PERSIST_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

def retrieve_chunks(query: str, k: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    if not results or not results["documents"]:
        return []

    docs = []
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        docs.append({
            "text": doc,
            "metadata": meta
        })

    return docs
