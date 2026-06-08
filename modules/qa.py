from utils.llm import ask_llm
from utils.prompt_loader import load_prompt

from utils.embeddings import get_embedding
from utils.vector_store import retrieve_chunks


def answer_question(question):

    query_embedding = get_embedding(
        question
    )

    chunks = retrieve_chunks(
        query_embedding,
        n_results=3
    )

    context = "\n\n".join(chunks)

    system_prompt = load_prompt(
        "prompts/rag_prompt.txt"
    )

    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    answer = ask_llm(
        system_prompt=system_prompt,
        user_prompt=user_prompt
    )

    return answer