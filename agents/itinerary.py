from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def create_itinerary(parsed_data, research_data):
    """
    Itinerary Agent:
    Creates a realistic day-by-day travel plan using parsed user needs and research results.
    """

    system_prompt = load_prompt("itinerary.txt")

    user_prompt = f"""
    Parsed user request:
    {parsed_data}

    Research data:
    {research_data}

    Create a day-by-day itinerary.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=900
    )

    return response.choices[0].message.content