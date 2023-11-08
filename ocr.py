import os
from dotenv import load_dotenv
import requests
import json
load_dotenv(dotenv_path="./.env")


def ocr_space_file(filename, overlay=False, api_key=os.getenv("OCR_API"), language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language}
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload)
    return r.content.decode()