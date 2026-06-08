import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from utils.embeddings import get_embedding


def test_embedding_generation():
    text = "Vision Transformer achieved 96.5% accuracy."

    embedding = get_embedding(text)

    print(type(embedding))
    print(len(embedding))
    print(embedding[:5])

    assert embedding is not None
    assert isinstance(embedding, list)
    assert len(embedding) > 0