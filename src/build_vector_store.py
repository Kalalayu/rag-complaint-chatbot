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
