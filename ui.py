import streamlit as st
import os
from dotenv import load_dotenv
from chatbot import Chatbot

# Load environment variables from .env file
load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

# Page title
st.title("Iota")

# Initialize the Chatbot object once and persist it across reruns
# session_state keeps variables alive between Streamlit interactions
if "bot" not in st.session_state:
    st.session_state.bot = Chatbot(key)

# Initialize empty conversation history for display
if "messages" not in st.session_state:
    st.session_state.messages = []

# Re-render all previous messages on every rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

try:
    if user_input := st.chat_input("Say something..."):

        # Display and store the user's message
        st.session_state.messages.append(
            {"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        # Send to AI and get reply — ONE API call, stored in variable to avoid multiple calls
        bot_reply = st.session_state.bot.send_message(user_input)

        # Display and store the bot's reply
        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply})
        with st.chat_message("assistant"):
            st.write(bot_reply)

except Exception as e:
    st.write("Something went wrong!", e)
