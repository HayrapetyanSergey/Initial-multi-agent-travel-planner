# Multi-Agent AI Travel Planner

## Project Overview

This project is a fully functional multi-agent artificial intelligence system designed to generate personalized travel plans through collaboration between multiple specialized AI agents.

The system accepts a natural language travel request from the user and processes it through several AI agents responsible for different tasks such as:

- request understanding,
- travel research,
- itinerary generation,
- budget estimation,
- quality evaluation,
- and final response generation.

The final output is a structured and professional travel recommendation including destination summaries, day-by-day itineraries, estimated costs, travel tips, and evaluation feedback.

The project also includes a conversational Streamlit web application that allows users to continue the conversation and modify previously generated travel plans.

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
- validate generated plans,
- support conversational follow-up requests,
- and produce structured final responses.

---

# System Architecture

The system uses 7 specialized AI agents.

## 1. Input Parser Agent

Extracts structured information from the user's request:

- destination
- trip duration
- budget
- interests
- travel style

---

## 2. Research Agent

Collects destination-related travel information.

The agent first checks the local travel knowledge base.

If the destination is unavailable locally, the agent dynamically generates AI-based travel research.

---

## 3. Itinerary Agent

Creates a realistic day-by-day travel itinerary based on:

- user interests,
- research data,
- destination information,
- and travel constraints.

---

## 4. Budget Agent

Estimates approximate:

- hotel costs,
- food costs,
- transportation costs,
- activity costs.

The agent also determines whether the trip fits the user's budget.

---

## 5. Critic Agent

Evaluates the generated travel plan using:

- completeness,
- practicality,
- budget fit,
- faithfulness to research data.

The agent provides:

- scores from 1–5,
- strengths,
- weaknesses,
- improvement suggestions,
- and final recommendations.

---

## 6. Final Response Agent

Combines all agent outputs into one clean, professional, and structured travel recommendation.

---

## 7. Conversation Context Agent

Handles follow-up user requests such as:

- “make it cheaper”
- “add more nature”
- “remove museums”
- “suggest another version”

This agent rewrites conversational follow-up messages into complete standalone travel requests using previous context.

---

# Workflow

```text
User Input
↓
Conversation Context Agent (optional)
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
```

---

# Features

- Multi-agent architecture
- Conversational travel planning
- Dynamic AI research fallback
- Structured JSON execution logs
- Budget estimation
- Travel plan evaluation
- Streamlit web application
- Follow-up itinerary modifications
- Local travel knowledge base
- AI-generated worldwide destination support

---

# Technologies Used

- Python 3.10+
- OpenAI API
- GPT-4.1-mini
- Streamlit
- python-dotenv
- JSON
- GitHub
- Streamlit Community Cloud

---

# Project Structure

```text
multi-agent-travel-planner/
├── agents/
│   ├── input_parser.py
│   ├── researcher.py
│   ├── itinerary.py
│   ├── budget.py
│   ├── critic.py
│   ├── final_response.py
│   └── conversation_handler.py
│
├── prompts/
│   ├── input_parser.txt
│   ├── researcher.txt
│   ├── itinerary.txt
│   ├── critic.txt
│   ├── budget.txt
│   └── final_response.txt
│
├── data/
│   └── travel_knowledge_base.json
│
├── runs/
│   └── execution_logs.json
│
├── utils/
│   ├── logger.py
│   └── prompt_loader.py
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <repository_url>
cd multi-agent-travel-planner
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create `.env` File

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# Run Instructions

## Terminal Version

Run the CLI application:

```bash
python main.py
```

Example request:

```text
I want a 7-day trip to Japan under $2500 focused on anime, food, and technology.
```

---

## Streamlit Web App

Run the web application locally:

```bash
streamlit run app.py
```

The web app supports:

- interactive travel planning,
- conversational follow-up requests,
- itinerary regeneration,
- and agent output inspection.

---

# Example Follow-Up Requests

```text
Make it cheaper
```

```text
Add more nature and less nightlife
```

```text
Replace Florence with Milan
```

```text
Suggest another version
```

---

# Output Structure

The system generates:

- user request,
- parsed structured data,
- travel research,
- itinerary,
- budget analysis,
- critic evaluation,
- final structured recommendation.

The system also stores complete execution traces inside the `runs/` folder as JSON logs.

---

# Data Sources

The system uses:

1. Local travel knowledge base (`travel_knowledge_base.json`)
2. AI-generated fallback travel research

This creates a hybrid research architecture:

- local structured data,
- plus dynamic worldwide AI support.

---

# Deployment

The application is deployed using Streamlit Community Cloud.

Deployment configuration:

- Repository: GitHub
- Main file: `app.py`
- Secrets management through Streamlit Secrets

Example Streamlit Secrets configuration:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

The API key is never stored directly in the repository.

---

# Error Handling

The system handles:

- missing destinations,
- invalid budgets,
- unclear user requests,
- missing local data,
- JSON parsing failures,
- missing travel constraints.

Fallback AI generation is used whenever local destination data is unavailable.

---

# Security Considerations

The project follows basic API security practices:

- API keys stored in `.env`
- `.gitignore` prevents secret uploads
- Streamlit Secrets used for deployment
- No hardcoded credentials

Potential production improvements:

- authentication,
- rate limiting,
- prompt injection protection,
- request validation.

---

# Limitations

- Travel prices are approximate and not live.
- Real-time travel APIs are not integrated.
- Flight booking functionality is not included.
- AI-generated research may vary between runs.
- Some destinations may contain less detailed information.

---

# Possible Improvements

- Add real-time travel APIs
- Add hotel booking integration
- Add flight booking APIs
- Add Google Maps integration
- Add weather forecasting
- Add restaurant recommendation APIs
- Add multilingual support
- Add user authentication
- Add persistent travel history

---

# Example Run Logs

Example execution traces are available inside the `runs/` folder.

Each log includes:

- agent prompts,
- agent outputs,
- user input,
- final responses,
- timestamps.

---

# Author

Sergey Hayrapetyan