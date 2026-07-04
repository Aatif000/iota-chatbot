import anthropic


class Chatbot:
    def __init__(self, API_KEY):
        self.api_key = API_KEY
        self.history = []
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def send_message(self, user_input):
        system_rules = [
            "You are Iota, a helpful, humorous and friendly AI assistant.",
            "You give clear, concise answers.",
            "You are honest when you don't know something and don't make things up.",
        ]
        system_prompt = " ".join(system_rules)
        self.history.append({"role": "user", "content": user_input})
        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=system_prompt,
            messages=self.history[-10:]
        )
        self.history.append(
            {"role": "assistant", "content": response.content[0].text})
        return response.content[0].text
