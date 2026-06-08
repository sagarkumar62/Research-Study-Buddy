import chromadb
import uuid
import numpy as np

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="research_papers"
)


def store_chunks(chunks, embeddings):
    ids = [
        str(uuid.uuid4())
        for _ in chunks
    ]

    # FIX: Convert numpy array matrix or nested arrays into a clean list of lists
    cleaned_embeddings = []
    for emb in embeddings:
        if isinstance(emb, np.ndarray):
            cleaned_embeddings.append(emb.tolist())
        elif hasattr(emb, "tolist"):
            cleaned_embeddings.append(emb.tolist())
        else:
            # Fallback: convert individual numpy float32 elements inside a list
            cleaned_embeddings.append([float(x) for x in emb])

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=cleaned_embeddings,  # Pass the cleaned Python list
        metadatas=[
            {"chunk_number": i}
            for i in range(len(chunks))
        ]
    )


def retrieve_chunks(
    query_embedding,
    n_results=3
):
    # FIX: Convert the single query embedding to a plain list if it's a numpy array
    if isinstance(query_embedding, np.ndarray):
        query_embedding = query_embedding.tolist()
    elif hasattr(query_embedding, "tolist"):
        query_embedding = query_embedding.tolist()
    else:
        query_embedding = [float(x) for x in query_embedding]

    results = collection.query(
        query_embeddings=[query_embedding],  # Pass the cleaned list
        n_results=n_results
    )

    return results["documents"][0]

# print(collection.count())