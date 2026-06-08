import re


def clean_text(text):
    """
    Clean extracted PDF text
    """

    # remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()