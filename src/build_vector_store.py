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
import pandas as pd
from src.config import DATA_PROCESSED, VECTOR_STORE
from src.chunking import chunk_text
from src.embedding import create_vector_store
from src.sampling import stratified_sample


# Load cleaned dataset from Task 1
df = pd.read_csv(DATA_PROCESSED / "filtered_complaints.csv")

if df.empty:
    raise RuntimeError("Cleaned dataset is empty. Run Task 1 first.")

# df = pd.read_csv(DATA_PROCESSED / "filtered_complaints.csv")

df = stratified_sample(
    df,
    group_col="Product",
    n_samples=12000
)

texts, metadata = [], []

for _, row in df.iterrows():
    chunks = chunk_text(row["clean_complaint"])
    for i, chunk in enumerate(chunks):
        texts.append(chunk)
        metadata.append({
            "product": row["Product"],
            "chunk_id": i
        })
create_vector_store(texts, metadata, VECTOR_STORE)
print("Vector store successfully created.")
