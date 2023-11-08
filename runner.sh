#!/bin/bash
python3 ./window_selector/window_selector.py
POINTS=$(<points.json)
python3 code_assistant.py "$POINTS"