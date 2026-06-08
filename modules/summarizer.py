from utils.llm import ask_llm
from utils.prompt_loader import load_prompt


def generate_summary(text):

    system_prompt = load_prompt(
        "prompts/summarizer_prompt.txt"
    )

    if system_prompt is None:
        raise ValueError(
            "Summarizer prompt could not be loaded."
        )

    summary = ask_llm(
        system_prompt=system_prompt,
        user_prompt=text
    )

    return summary


def generate_summary_from_chunks(chunks):

    batch_size = 10
    batch_summaries = []

    for i in range(0, len(chunks), batch_size):

        batch = chunks[i:i + batch_size]

        combined = "\n\n".join(batch)

        summary = generate_summary(combined)

        batch_summaries.append(summary)

    final_summary = generate_summary(
        "\n\n".join(batch_summaries)
    )

    return final_summary