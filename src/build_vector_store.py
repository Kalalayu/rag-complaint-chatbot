import pyarrow.parquet as pq
import chromadb
from chromadb.config import Settings
from tqdm import tqdm
import os

# -----------------------------
# Config
# -----------------------------
DATA_PATH = "data/raw/complaint_embeddings.parquet"
VECTOR_DB_DIR = "vector_store"
COLLECTION_NAME = "complaints"
BATCH_SIZE = 1000

def main():
    print("🚀 Loading parquet data in streaming mode...")

    os.makedirs(VECTOR_DB_DIR, exist_ok=True)

    client = chromadb.Client(
        Settings(
            persist_directory=VECTOR_DB_DIR,
            anonymized_telemetry=False
        )
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    parquet_file = pq.ParquetFile(DATA_PATH)

    total_batches = parquet_file.num_row_groups
    print(f"📦 Total row groups: {total_batches}")

    for i in tqdm(range(total_batches), desc="Indexing batches"):
        batch = parquet_file.read_row_group(i).to_pandas()

        documents = batch["document"].tolist()
        embeddings = batch["embedding"].tolist()
        metadatas = batch["metadata"].tolist()

        ids = [f"{meta['complaint_id']}_{meta['chunk_index']}" for meta in metadatas]

        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    client.persist()
    print("✅ Vector store built and persisted successfully")

MAX_ROWS = 5000  # safe for laptop
import pyarrow.parquet as pq

table = pq.read_table(
    DATA_PATH,
    columns=["document", "embedding", "metadata"]
).slice(0, MAX_ROWS)

df = table.to_pandas()

if __name__ == "__main__":
    main()
