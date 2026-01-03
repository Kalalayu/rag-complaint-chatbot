import pandas as pd
from src.config import DATA_PROCESSED, VECTOR_STORE
from src.preprocessing import clean_text
from src.chunking import chunk_text
from src.embedding import create_vector_store

# Load data
df = pd.read_csv(DATA_PROCESSED / "filtered_complaints.csv")

# Clean text
df["clean_text"] = df["clean_complaint"].apply(clean_text)

chunks = []
metadata = []

for _, row in df.iterrows():
    parts = chunk_text(row["clean_text"])
    for i, chunk in enumerate(parts):
        chunks.append(chunk)
        metadata.append({
            "complaint_id": row.get("Complaint ID", ""),
            "product": row["Product"],
            "chunk_id": i
        })
if df.empty:
    raise ValueError("Input dataset is empty. Check preprocessing step.")

# Create vector store
create_vector_store(chunks, metadata, VECTOR_STORE)
