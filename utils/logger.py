import json
import os
from datetime import datetime
from utils.prompt_loader import load_prompt


def save_run_log(
    user_input,
    parsed_data,
    research_data,
    itinerary_data,
    budget_data,
    critic_data,
    final_response
):
    """
    Saves a structured run trace to runs/<timestamp>.json
    """

    os.makedirs("runs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"runs/{timestamp}.json"

    run_log = {
        "timestamp": timestamp,
        "user_input": user_input,

        "agent_prompts": {
            "input_parser_prompt": load_prompt("input_parser.txt"),
            "researcher_prompt": load_prompt("researcher.txt"),
            "itinerary_prompt": load_prompt("itinerary.txt"),
            "budget_prompt": load_prompt("budget.txt"),
            "critic_prompt": load_prompt("critic.txt"),
            "final_response_prompt": load_prompt("final_response.txt")
        },

        "agent_outputs": {
            "input_parser_agent": parsed_data,
            "research_agent": research_data,
            "itinerary_agent": itinerary_data,
            "budget_agent": budget_data,
            "critic_agent": critic_data,
            "final_response_agent": final_response
        },

        "final_answer": final_response
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(run_log, file, indent=4, ensure_ascii=False)

    return file_path