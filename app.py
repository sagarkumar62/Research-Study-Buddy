# from utils.pdf_loader import extract_text_from_pdf

# pdf_text = extract_text_from_pdf("data/sample.pdf")

# print(pdf_text[:1000])

from utils.embeddings import get_embedding

text = "Vision Transformer achieved 96.5% accuracy"

vector = get_embedding(text)

print(type(vector))
print(len(vector))
print(vector[:10])

# app.py

# from utils.llm import ask_llm

# response = ask_llm(
#     "Explain RAG in 3 lines."
# )

# print(response)

# from modules.summarizer import generate_summary

# sample_text = """
# In this work, we compare ResNet50 and
# Vision Transformer on CIFAR-10.

# ResNet achieved 93.2% accuracy.

# Vision Transformer achieved 96.5% accuracy.

# Training was performed using NVIDIA A100 GPUs.
# """

# summary = generate_summary(sample_text)

# print(summary)

# from modules.extractor import extract_entities_from_chunks

# chunks = [
#     "ResNet50 achieved 93.2% accuracy on CIFAR-10",
#     "Vision Transformer achieved 96.5% accuracy on CIFAR-10 using NVIDIA A100 GPUs"
# ]

# entities = extract_entities_from_chunks(chunks)

# print(entities)

# from modules.table_generator import generate_table

# sample_data = {
#     "models": [
#         "ResNet50",
#         "Vision Transformer"
#     ],
#     "datasets": [
#         "CIFAR-10"
#     ],
#     "metrics": [
#         "93.2%",
#         "96.5%"
#     ],
#     "hardware": [
#         "NVIDIA A100"
#     ]
# }

# table = generate_table(sample_data)

# print(table)