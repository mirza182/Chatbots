import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

class FriendlyChatbot:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a friendly chatbot designed to assist users in a warm and supportive manner."}
        ]

    def get_response(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use your specific model here
            messages=self.messages
        )
        reply = response['choices'][0]['message']['content']
        self.messages.append({"role": "assistant", "content": reply})
        return reply
