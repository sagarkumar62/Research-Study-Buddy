import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env")

print(f"Loaded API Key: {api_key[:10]}...")

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

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=final_prompt
            )

            return response.text

        except Exception as e:

            print(
                f"Attempt {attempt + 1}/{max_retries} failed: {e}"
            )

            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)
                print(
                    f"Retrying in {wait_time} seconds..."
                )
                time.sleep(wait_time)

            else:
                raise Exception(
                    f"Gemini API failed after {max_retries} attempts.\n{e}"
                )