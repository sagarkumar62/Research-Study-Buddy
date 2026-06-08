from utils.embeddings import get_embedding

text = "Vision Transformer achieved 96.5% accuracy."

embedding = get_embedding(text)

print(type(embedding))
print(len(embedding))
print(embedding[:5])