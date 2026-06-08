from utils.embeddings import get_embedding
from utils.vector_store import retrieve_chunks


def get_relevant_context(question):

    query_embedding = get_embedding(
        question
    )

    chunks = retrieve_chunks(
        query_embedding,
        n_results=2
    )

    return "\n\n".join(chunks)