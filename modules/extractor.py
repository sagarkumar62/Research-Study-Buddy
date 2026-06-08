import json

from utils.llm import ask_llm
from utils.prompt_loader import load_prompt


def extract_entities(text):

    system_prompt = load_prompt(
        "prompts/extractor_prompt.txt"
    )

    response = ask_llm(
        system_prompt=system_prompt,
        user_prompt=text
    )

    if response is None:
        return {
        "models": [],
        "datasets": [],
        "metrics": [],
        "hardware": [],
        "hyperparameters": [],
        "algorithms": [],
        "key_findings": [],
        "limitations": []
    }

    # Remove markdown code fences
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        print("Failed to parse JSON")

        return {
            "models": [],
            "datasets": [],
            "metrics": [],
            "hardware": [],
            "hyperparameters": [],
            "algorithms": [],
            "key_findings": [],
            "limitations": []
        }


def extract_entities_from_chunks(chunks):

    merged_data = {
        "models": set(),
        "datasets": set(),
        "metrics": set(),
        "hardware": set(),
        "hyperparameters": set(),
        "algorithms": set(),
        "key_findings": set(),
        "limitations": set()
    }

    for chunk in chunks:

        try:
            result = extract_entities(chunk)

        except Exception as e:
            print(f"Chunk failed: {e}")
            continue

        for key in merged_data:

            if key in result:
                merged_data[key].update(result[key])

    final_data = {
        key: list(value)
        for key, value in merged_data.items()
    }

    return final_data


