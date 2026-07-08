from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_fields(text):

    with open(
        "prompts/extraction_prompt.txt",
        "r",
        encoding="utf-8"
) as f:

        prompt = f.read()

    final_prompt = f"""
{prompt}

FNOL Document:

{text}
"""
    
    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=final_prompt
        )

        output = response.text.strip()

        # Remove markdown if Gemini returns it
        output = output.replace("```json", "")
        output = output.replace("```", "")
        output = output.strip()

        return json.loads(output)

    except json.JSONDecodeError:

        return {
            "error": "Gemini returned invalid JSON.",
            "raw_output": output
        }

    except Exception as e:

        return {
            "error": str(e)
        }