def load_prompt(file_path):
    """
    Load prompt text from a file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Prompt file not found: {file_path}")
        return None