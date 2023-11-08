import json
import os
from pynput import keyboard
from api import ChatBot

from app import ocr_space_file, screen_capture


class KeyboardListener:
    def __init__(self, points):
        self.points = points
        self.listener = keyboard.Listener(on_press=self.on_press)
        api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI API key
        self.chat_bot = ChatBot(api_key)
        
    def on_press(self, key):
        try:
            if key == keyboard.Key.up:
                filename = screen_capture(self.points)
                text = json.loads(ocr_space_file(filename))
                self.chat_bot.chat({"role": "user", "content": text['ParsedResults'][0]['ParsedText']})

        except AttributeError:
            pass

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()