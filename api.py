import openai

class ChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = [
            {"role": "system",
             "content": "You are a code interview assistant, I will provide segments from a coding assessment. Your task is to identify any questions within the text and respond to them concisely and accurately."}
        ]

    def chat(self, message):
        self.messages.append(message)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        chat_message = response['choices'][0]['message']['content']
        print("\n")
        print(f"Bot: {chat_message}")
        print("\n -------------------------")
        self.messages.append({"role": "assistant", "content": chat_message})