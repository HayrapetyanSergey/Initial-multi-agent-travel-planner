# Multi-Agent AI Travel Planner

## Project Overview

This project is a fully functional multi-agent artificial intelligence system designed to generate personalized travel plans.

The system accepts a user travel request at runtime and processes it through multiple specialized AI agents. Each agent has a unique responsibility such as input understanding, travel research, itinerary generation, budget estimation, answer validation, and final response generation.

The final output is a structured travel recommendation including destination insights, day-by-day itinerary, budget analysis, travel tips, and quality evaluation.

---

# Domain

Travel Planning / AI-Powered Trip Assistance

---

# Goal

The goal of the project is to demonstrate how multiple AI agents can cooperate together to solve a complex real-world task more effectively than a single chatbot.

The system is designed to:
- understand user travel requests,
- gather travel information,
- generate realistic itineraries,
- estimate travel costs,
- validate the generated plan,
- and produce a final structured answer.

---

# System Architecture

The system uses 6 specialized AI agents:

## 1. Input Parser Agent
Extracts structured information from the user's request:
- destination
- trip duration
- budget
- interests
- travel style

## 2. Research Agent
Collects destination-related travel information.

The agent first checks the local knowledge base.  
If the destination is unavailable locally, the agent generates AI-based travel research dynamically.

## 3. Itinerary Agent
Creates a realistic day-by-day travel itinerary based on:
- user interests
- research data
- destination information

## 4. Budget Agent
Estimates approximate:
- hotel costs
- food costs
- transportation costs
- activity costs

The agent also determines whether the trip fits the user's budget.

## 5. Critic Agent
Evaluates the generated travel plan using:
- completeness
- practicality
- budget fit
- faithfulness to research data

The agent provides scores from 1–5 and improvement suggestions.

## 6. Final Response Agent
Combines all agent outputs into one professional and structured final answer.

---

# Workflow

User Input
↓
Input Parser Agent
↓
Research Agent
↓
Itinerary Agent
↓
Budget Agent
↓
Critic Agent
↓
Final Response Agent
↓
JSON Run Log

---

# Technologies Used

- Python 3.10+
- OpenAI API
- GPT-4.1-mini
- python-dotenv
- rich

---

# Project Structure

```text
multi-agent-travel-planner/
├── agents/
├── prompts/
├── data/
├── runs/
├── utils/
├── main.py
├── requirements.txt
├── README.md
└── .env
```

# Setup Instructions

## 1. Clone the repository

```bash
git clone <repository_url>
cd multi-agent-travel-planner
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create .env file

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

# Run Instructions

Run the application:

```bash
python main.py
```

Then enter a travel request such as:

```text
I want a 7-day trip to Japan under $2500 focused on anime, food, and technology.
```

# Output Structure

The system outputs:
- User question
- Agent 1 output
- Agent 2 output
- Agent 3 output
- Agent 4 output
- Agent 5 output
- Final structured answer

The system also saves structured JSON execution traces inside the `runs/` folder.

# Data Sources

The system uses:
1. Local travel knowledge base (`travel_knowledge_base.json`)
2. AI-generated fallback research for unknown destinations

# Error Handling

The system handles:
- missing destinations
- invalid budgets
- unclear user requests
- missing local data
- JSON parsing failures

# Limitations

- Travel prices are approximate and not live.
- The system does not currently use real-time APIs.
- Flight booking integration is not included.
- Some destinations may have less detailed AI-generated research.

# Possible Improvements

- Add real-time travel APIs
- Add hotel and flight booking integration
- Add Streamlit web interface
- Add Google Maps integration
- Add weather forecasts
- Add restaurant recommendation APIs

# Example Run Logs

Example JSON traces are available inside the `runs/` folder.

# Author

Sergey Hayrapetyan