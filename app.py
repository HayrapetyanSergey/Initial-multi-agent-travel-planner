import streamlit as st

from agents.input_parser import parse_user_input
from agents.researcher import research_destination
from agents.itinerary import create_itinerary
from agents.budget import estimate_budget
from agents.critic import evaluate_plan
from agents.final_response import generate_final_response
from agents.conversation_handler import rewrite_follow_up_request
from utils.logger import save_run_log


st.set_page_config(
    page_title="Multi-Agent AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ Multi-Agent AI Travel Planner")
st.write("Ask for a travel plan and continue the conversation to modify it.")

# Session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "last_plan" not in st.session_state:
    st.session_state["last_plan"] = None


# Show chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input(
    "Ask for a travel plan or modify the previous one..."
)

if user_input:
    st.session_state["messages"].append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Agents are working..."):

            # If there is a previous plan, rewrite follow-up into a full request
            if st.session_state["last_plan"]:
                effective_user_input = rewrite_follow_up_request(
                    st.session_state["last_plan"],
                    user_input
                )
            else:
                effective_user_input = user_input

            parsed_data = parse_user_input(effective_user_input)

            if not parsed_data.get("destination"):
                error_message = "Destination is missing. Please provide a country or city for the trip."
                st.error(error_message)
                st.session_state["messages"].append(
                    {"role": "assistant", "content": error_message}
                )
                st.stop()

            research_data = research_destination(parsed_data)
            itinerary_data = create_itinerary(parsed_data, research_data)
            budget_data = estimate_budget(parsed_data, research_data, itinerary_data)
            critic_data = evaluate_plan(parsed_data, research_data, itinerary_data, budget_data)

            final_response = generate_final_response(
                effective_user_input,
                parsed_data,
                research_data,
                itinerary_data,
                budget_data,
                critic_data
            )

            log_file = save_run_log(
                effective_user_input,
                parsed_data,
                research_data,
                itinerary_data,
                budget_data,
                critic_data,
                final_response
            )

            st.session_state["last_plan"] = final_response

        st.markdown(final_response)

        with st.expander("See agent outputs"):
            st.write("Effective request used by the system:")
            st.info(effective_user_input)

            st.subheader("Agent 1 — Input Parser")
            st.json(parsed_data)

            st.subheader("Agent 2 — Research Agent")
            st.json(research_data)

            st.subheader("Agent 3 — Itinerary Agent")
            st.markdown(itinerary_data)

            st.subheader("Agent 4 — Budget Agent")
            st.json(budget_data)

            st.subheader("Agent 5 — Critic Agent")
            st.json(critic_data)

            st.info(f"Run log saved to: `{log_file}`")

    st.session_state["messages"].append(
        {"role": "assistant", "content": final_response}
    )


if st.sidebar.button("Clear conversation"):
    st.session_state["messages"] = []
    st.session_state["last_plan"] = None
    st.rerun()