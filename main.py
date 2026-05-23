from agents.input_parser import parse_user_input
from agents.researcher import research_destination
from agents.itinerary import create_itinerary
from agents.budget import estimate_budget
from agents.critic import evaluate_plan
from agents.final_response import generate_final_response
from utils.logger import save_run_log

from rich import print

# Ask user for travel request
user_input = input("Enter your travel request: ")

# Agent 1 — Input Parser
parsed_data = parse_user_input(user_input)

# Handle unclear or missing destination
if not parsed_data.get("destination"):
    print("\n[bold red]ERROR:[/bold red]\n")
    print("Destination is missing. Please provide a country or city for the trip.")
    exit()

# Agent 2 — Research Agent
research_data = research_destination(parsed_data)

# Agent 3 — Itinerary Agent
itinerary_data = create_itinerary(parsed_data, research_data)

# Agent 4 — Budget Agent
budget_data = estimate_budget(
    parsed_data,
    research_data,
    itinerary_data
)

# Agent 5 — Critic Agent
critic_data = evaluate_plan(
    parsed_data,
    research_data,
    itinerary_data,
    budget_data
)

# Final Response Agent
final_response = generate_final_response(
    user_input,
    parsed_data,
    research_data,
    itinerary_data,
    budget_data,
    critic_data
)

# Save run log
log_file = save_run_log(
    user_input,
    parsed_data,
    research_data,
    itinerary_data,
    budget_data,
    critic_data,
    final_response
)

# =========================
# DISPLAY OUTPUTS
# =========================

print("\n[bold green]USER QUESTION:[/bold green]\n")
print(user_input)

print("\n[bold green]AGENT 1 OUTPUT - INPUT PARSER:[/bold green]\n")
print(parsed_data)

print("\n[bold cyan]AGENT 2 OUTPUT - RESEARCH AGENT:[/bold cyan]\n")
print(research_data)

print("\n[bold magenta]AGENT 3 OUTPUT - ITINERARY AGENT:[/bold magenta]\n")
print(itinerary_data)

print("\n[bold yellow]AGENT 4 OUTPUT - BUDGET AGENT:[/bold yellow]\n")
print(budget_data)

print("\n[bold red]AGENT 5 OUTPUT - CRITIC AGENT:[/bold red]\n")
print(critic_data)

print("\n[bold white on blue]FINAL STRUCTURED ANSWER:[/bold white on blue]\n")
print(final_response)

print("\n[bold blue]RUN LOG SAVED TO:[/bold blue]\n")
print(log_file)