import json
import os
import signal
import time

from dotenv import load_dotenv
from ocr import ocr_space_file
from api import ChatBot
from keyboard_listener import KeyboardListener
from PIL import ImageGrab
from datetime import datetime
load_dotenv(dotenv_path="./.env")

def screen_capture(points):
    p1, p2 = points[0], points[1]
    x0, y0 = p1
    x1, y1 = p2
    img = ImageGrab.grab(bbox=(x0, y0, x1, y1), include_layered_windows=True)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshot_{timestamp}.png'
    img.save(filename)
    return filename

def main(points):
    listener = KeyboardListener(points)
    listener.start()



if __name__ == "__main__":
    import sys
    points_arg = sys.argv[1] if len(sys.argv) > 1 else '[]'
    points = json.loads(points_arg)
    main(points)