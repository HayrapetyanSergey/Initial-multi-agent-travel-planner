from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def evaluate_plan(parsed_data, research_data, itinerary_data, budget_data):
    """
    Critic Agent:
    Evaluates the final travel plan using multiple quality dimensions.
    """

    system_prompt = load_prompt("critic.txt")

    user_prompt = f"""
    Parsed user request:
    {parsed_data}

    Research data:
    {research_data}

    Itinerary:
    {itinerary_data}

    Budget analysis:
    {budget_data}

    Evaluate the plan.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=700
    )

    result = response.choices[0].message.content.strip()

    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(result)
    except Exception:
        return {
            "error": "Failed to parse critic JSON",
            "raw_output": result
        }