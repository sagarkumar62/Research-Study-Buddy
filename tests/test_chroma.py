import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from utils.embeddings import get_embedding
from utils.vector_store import store_chunks

chunks = [
    "ResNet50 achieved 93.2% accuracy.",
    "Vision Transformer achieved 96.5% accuracy.",
    "Training used NVIDIA A100 GPUs."
]

embeddings = [
    get_embedding(chunk)
    for chunk in chunks
]

store_chunks(
    chunks,
    embeddings
)

print("Stored successfully")