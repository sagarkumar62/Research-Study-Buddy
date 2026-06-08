# test_context.py
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from modules.retriever import (
    get_relevant_context
)

question = (
    "Which model achieved highest accuracy?"
)

context = get_relevant_context(
    question
)

print(context)