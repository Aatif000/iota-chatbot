# Iota - AI Chatbot

A conversational AI chatbot built with Python and Claude API by Anthropic.
Features a clean web UI and persistent conversation memory.

## Features

- Real-time AI responses powered by Claude (Haiku 4.5)
- Conversation memory — Iota remembers context within a session
- Clean chat UI built with Streamlit
- Secure API key management with environment variables
- Conversation logging to local file

## Tech Stack

- Python
- Anthropic Claude API
- Streamlit
- python-dotenv

## Installation

1. Clone the repository
   git clone https://github.com/Aatif000/iota-chatbot.git
   cd iota-chatbot

2. Install dependencies
   pip install anthropic streamlit python-dotenv

3. Create a .env file in the root directory
   ANTHROPIC_API_KEY=your_api_key_here

4. Run the app
   streamlit run ui.py

## Project Structure

- chatbot.py → Chatbot class, API integration, conversation memory
- ui.py → Streamlit web interface
- app.py → Terminal version with conversation logging

## Live Demo

[Try Iota here](https://iota-chatbot-1.streamlit.app)

## Author

Mohammed Aatif Minhaj
