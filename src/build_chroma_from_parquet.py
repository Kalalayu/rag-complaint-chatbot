# src/build_chroma_from_parquet.py

import duckdb
import chromadb
from chromadb.config import Settings

PARQUET_PATH = "data/raw/complaint_embeddings.parquet"
PERSIST_DIR = "vector_store"
COLLECTION_NAME = "complaints"
BATCH_SIZE = 1000

print("🚀 Initializing Chroma...")
client = chromadb.Client(
    Settings(
        persist_directory=PERSIST_DIR,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

print("🚀 Streaming parquet with DuckDB...")
con = duckdb.connect()

offset = 0
total_inserted = 0

while True:
    query = f"""
        SELECT document, metadata, embedding
        FROM read_parquet('{PARQUET_PATH}')
        LIMIT {BATCH_SIZE} OFFSET {offset}
    """
    batch = con.execute(query).fetch_df()

    if batch.empty:
        break

    collection.add(
        ids=[str(offset + i) for i in range(len(batch))],
        documents=batch["document"].tolist(),
        metadatas=batch["metadata"].tolist(),
        embeddings=batch["embedding"].tolist()
    )

    total_inserted += len(batch)
    offset += BATCH_SIZE

    print(f"✅ Inserted {total_inserted} documents...")

client.persist()
print(f"🎉 DONE! Total documents inserted: {total_inserted}")
