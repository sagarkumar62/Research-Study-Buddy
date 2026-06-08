import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.embeddings import get_embedding
from utils.vector_store import retrieve_chunks

query = "Which model achieved highest accuracy?"

query_embedding = get_embedding(query)

results = retrieve_chunks(
    query_embedding,
    n_results=2
)

print(results)