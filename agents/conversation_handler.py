from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def rewrite_follow_up_request(previous_plan, new_user_message):
    """
    Converts a follow-up message into a complete travel request using previous context.
    """

    system_prompt = """
    You are a conversation context agent for a travel planning system.

    The user may write a follow-up message like:
    - I don't like this, suggest another version
    - make it cheaper
    - add more nature
    - remove museums
    - replace this city

    Your task is to rewrite the follow-up into a complete standalone travel request.

    Use the previous travel plan as context.
    Return only the rewritten request as plain text.
    """

    user_prompt = f"""
    Previous travel plan:
    {previous_plan}

    New user message:
    {new_user_message}

    Rewrite this as a complete standalone travel request.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=300
    )

    return response.choices[0].message.content.strip()