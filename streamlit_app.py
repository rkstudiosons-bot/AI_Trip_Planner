import streamlit as st
import datetime
import requests
import os
import sys



BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Travel Planner Agentic Application",
    page_icon="🌍",
    layout = "centered",
    initial_sidebar_state = "expanded",
)



st.title("Travel Planner Agentic Application 🌍")

if "message" not in st.session_state:
    st.session_state.message = []


st.header("How can I help you plan your trip today? Let me know where you would like to visit today!")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="E.g., Plan a trip to Paris for 5 days with a budget of $2000")
    submit_button = st.form_submit_button("Send")


if submit_button and user_input.strip():
    
    try:
        with st.spinner("Planning your trip..."):
            payload = {"question": user_input}
            
            response = requests.post(
                f"{BASE_URL}/query",
                json=payload
            )
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                markdown_content = f"**User:** {user_input}\n\n**Travel Planner Agent:** {answer}\n\n---\n"
                st.markdown(markdown_content)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
