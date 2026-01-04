from sentence_transformers import SentenceTransformer
import faiss, json

def create_vector_store(texts, metadata, save_path):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, str(save_path / "index.faiss"))
    with open(save_path / "metadata.json", "w") as f:
        json.dump(metadata, f)
