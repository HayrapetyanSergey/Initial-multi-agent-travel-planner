from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_final_response(
    user_input,
    parsed_data,
    research_data,
    itinerary_data,
    budget_data,
    critic_data
):
    """
    Final Response Agent:
    Combines all agent outputs into one polished final answer.
    """

    system_prompt = load_prompt("final_response.txt")

    user_prompt = f"""
    User request:
    {user_input}

    Parsed data:
    {parsed_data}

    Research data:
    {research_data}

    Itinerary:
    {itinerary_data}

    Budget:
    {budget_data}

    Critic evaluation:
    {critic_data}

    Generate the final response.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1200
    )

    return response.choices[0].message.content