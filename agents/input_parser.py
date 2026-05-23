from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt

import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_user_input(user_input):
    """
    Extract structured travel information from user request.
    """

    system_prompt = load_prompt("input_parser.txt")

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        max_tokens=300
    )

    result = response.choices[0].message.content.strip()

    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    try:
        parsed_json = json.loads(result)
        return parsed_json

    except Exception:
        return {
            "error": "Failed to parse JSON",
            "raw_output": result
        }