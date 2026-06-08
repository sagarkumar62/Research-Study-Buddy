import json

from utils.llm import ask_llm
from utils.prompt_loader import load_prompt


def generate_table(extracted_data):

    table = "| Category | Values |\n"
    table += "|----------|--------|\n"

    for key, value in extracted_data.items():

        values = ", ".join(value) if value else "N/A"

        table += f"| {key} | {values} |\n"

    return table