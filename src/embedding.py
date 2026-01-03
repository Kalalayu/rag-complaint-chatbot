import faiss
import json
from sentence_transformers import SentenceTransformer
from pathlib import Path

def create_vector_store(texts, metadata, save_dir):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    save_dir.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(save_dir / "index.faiss"))

    with open(save_dir / "metadata.json", "w") as f:
        json.dump(metadata, f)

    return index
