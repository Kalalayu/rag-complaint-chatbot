# src/build_vector_store_small.py

import duckdb
import chromadb
from chromadb.config import Settings
from pathlib import Path
from tqdm import tqdm
import sys

# =========================
# ABSOLUTE PATHS (FIXED)
# =========================
DATA_PATH = r"C:\Users\Dell\Pictures\rag-complaint-chatbot\data\raw\complaint_embeddings.parquet"
VECTOR_DIR = Path(r"C:\Users\Dell\Pictures\rag-complaint-chatbot\vector_store")
COLLECTION_NAME = "complaints"
LIMIT_ROWS = 2000

def main():
    print("🚀 Building SMALL vector store (ABSOLUTE PATH – FINAL)")
    print(f"📄 Data file : {DATA_PATH}")
    print(f"📂 Vector dir: {VECTOR_DIR}")

    VECTOR_DIR.mkdir(exist_ok=True)

    # ---- Read parquet safely using DuckDB ----
    con = duckdb.connect(database=":memory:")
    df = con.execute(f"""
        SELECT id, document, metadata
        FROM read_parquet('{DATA_PATH}')
        LIMIT {LIMIT_ROWS}
    """).df()

    print(f"📦 Rows loaded: {len(df)}")

    # ---- Chroma persistent client ----
    client = chromadb.Client(
        Settings(
            persist_directory=str(VECTOR_DIR),
            anonymized_telemetry=False
        )
    )

    # Clean rebuild
    try:
        client.delete_collection(COLLECTION_NAME)
        print("🗑️ Old collection removed")
    except Exception:
        pass

    collection = client.create_collection(COLLECTION_NAME)

    for _, row in tqdm(df.iterrows(), total=len(df), desc="Indexing"):
        collection.add(
            ids=[str(row["id"])],
            documents=[row["document"]],
            metadatas=[row["metadata"]],
        )

    print("✅ Vector store built successfully")

    # FORCE flush
    del collection
    del client
    sys.exit(0)

if __name__ == "__main__":
    main()
