import os
from chatbot import Chatbot
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")

bot = Chatbot(key)

user_input = input("Type something..." + "\n")

with open("logs.txt", "a", encoding="utf-8") as f:
    f.write("\n" + "\t**New Converstaion**" + "\n")

while True:
    try:
        if user_input.lower() == "quit":
            break
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write("You: " + user_input + "\n")
        output = bot.send_message(user_input)
        print(output)
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write("Assistant: " + output + "\n")
        user_input = input("Reply..." + "\n")
    except:
        print(input("Something went wrong! Try again."))
