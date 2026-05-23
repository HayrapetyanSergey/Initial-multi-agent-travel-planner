import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_research(parsed_data):
    """
    AI fallback research:
    If destination is not found in the local knowledge base,
    this agent generates structured travel research using the LLM.
    """

    system_prompt = load_prompt("researcher.txt")

    user_prompt = f"""
    Parsed user request:
    {parsed_data}

    Generate travel research for this request.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=900
    )

    result = response.choices[0].message.content.strip()

    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(result)
    except Exception:
        return {
            "status": "error",
            "source": "ai_generated_research",
            "message": "AI research output could not be parsed as JSON.",
            "raw_output": result
        }


def research_destination(parsed_data):
    """
    Research Agent:
    First checks the local travel knowledge base.
    If destination is not found, it uses AI-generated research.
    """

    destination = parsed_data.get("destination")

    if not destination:
        return {
            "status": "missing_destination",
            "message": "Destination is missing. Please provide a country or city for the trip.",
            "source": "input_validation"
        }

    try:
        with open("data/travel_knowledge_base.json", "r", encoding="utf-8") as file:
            knowledge_base = json.load(file)

        if destination in knowledge_base:
            destination_data = knowledge_base[destination]
            interests = parsed_data.get("interests") or []
            matched_places = []

            for city_name, city_data in destination_data["cities"].items():
                for attraction in city_data["attractions"]:
                    attraction_text = (
                        attraction["name"] + " " +
                        attraction["category"] + " " +
                        attraction["description"]
                    ).lower()

                    if any(interest.lower() in attraction_text for interest in interests):
                        matched_places.append({
                            "city": city_name,
                            **attraction
                        })

            return {
                "status": "success",
                "source": "local_knowledge_base",
                "destination": destination,
                "currency": destination_data["currency"],
                "daily_cost_estimates": {
                    "hotel": destination_data["average_daily_hotel"],
                    "food": destination_data["average_daily_food"],
                    "transport": destination_data["average_daily_transport"]
                },
                "matched_places": matched_places,
                "travel_tips": destination_data["travel_tips"]
            }

        return generate_ai_research(parsed_data)

    except Exception as e:
        return {
            "status": "error",
            "source": "research_agent",
            "message": str(e)
        }