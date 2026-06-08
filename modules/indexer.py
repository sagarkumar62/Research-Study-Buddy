from utils.embeddings import get_embedding
from utils.vector_store import store_chunks


def index_chunks(chunks):

    embeddings = [
        get_embedding(chunk)
        for chunk in chunks
    ]

    store_chunks(
        chunks,
        embeddings
    )