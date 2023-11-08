import tkinter as tk
from PIL import ImageGrab
from datetime import datetime
from pynput import keyboard
import requests 
import json
import openai
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")
openai.api_key = os.getenv("OPENAI_API_KEY")
input = os.getenv("TEXT")

class Screenshotter:
    def __init__(self):
        self.root = tk.Tk()
        self.points = []

    def on_click(self, event):
        self.points.append((event.x_root, event.y_root))
        if len(self.points) == 2:
            self.root.quit()  # Hide the main window


    def run(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f'{screen_width}x{screen_height}+0+0')
        self.root.wm_attributes('-alpha',0.5)
        self.root.bind('<Button-1>', self.on_click)
        self.root.mainloop()
        return self.points

def screen_capture(points):
    p1, p2 = points[0], points[1]
    x0, y0 = p1
    x1, y1 = p2
    img = ImageGrab.grab(bbox=(x0, y0, x1, y1), include_layered_windows=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshot_{timestamp}.png'
    img.save(filename)
    text = json.loads(ocr_space_file(filename))
    print('Question ? ')
    chat({"role": "user", "content": text['ParsedResults'][0]['ParsedText']})

messages = [
    {"role": "system", "content": "You are a code interview assistant, I will provide segments from a coding assessment. Your task is to identify any questions within the text and respond to them concisely and accurately."},
  ]


def chat(message):
    messages.append(message)
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    chat_message = response['choices'][0]['message']['content']
    print("\n")
    print(f"Bot: {chat_message}")
    print("\n -------------------------")
    messages.append({"role": "assistant", "content": chat_message})

def ocr_space_file(filename, overlay=False, api_key='K84662968788957', language='eng'):

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def on_press(key):
    try:
        if key == keyboard.Key.up:
            screen_capture(points)

    except AttributeError:
        pass

# Start the pynput listener in a non-blocking fashion
listener = keyboard.Listener(on_press=on_press)
listener.start()
screenshotter = Screenshotter()
points = screenshotter.run()  # Get the points from the user
listener.join()
# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    listener.stop()
