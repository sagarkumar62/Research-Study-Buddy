import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print(api_key)


if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(
    api_key=api_key
)

def ask_llm(system_prompt, user_prompt):

    print("Gemini API Called")

    final_prompt = f"""
SYSTEM:
{system_prompt}

USER:
{user_prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=final_prompt
    )

    return response.text