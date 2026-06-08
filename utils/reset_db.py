# reset_db.py

import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

try:
    client.delete_collection(
        name="research_papers"
    )
    print("Collection deleted")
except Exception as e:
    print(e)