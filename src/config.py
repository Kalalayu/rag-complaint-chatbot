from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_RAW = BASE_DIR / "data" / "raw"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
VECTOR_STORE = BASE_DIR / "vector_store"

# Ensure directories exist
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
VECTOR_STORE.mkdir(parents=True, exist_ok=True)

