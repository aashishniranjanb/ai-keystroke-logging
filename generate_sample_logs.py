"""
Log Generator for Testing the Streamlit Dashboard
Creates realistic keystroke log entries for demonstration purposes
"""

import time
import random
from datetime import datetime, timedelta

LOG_FILE = "keylog_ai.txt"

# Sample inputs with their classifications
SAMPLE_LOGS = [
    ("hello world", "NORMAL INPUT", 3.2),
    ("testing this system", "NORMAL INPUT", 4.5),
    ("1234", "POSSIBLE PIN ENTRY", 0.8),
    ("5678", "POSSIBLE PIN ENTRY", 1.1),
    ("9012", "POSSIBLE PIN ENTRY", 0.9),
    ("password123!", "POSSIBLE PASSWORD ENTRY", 2.1),
    ("MySecure@2024", "POSSIBLE PASSWORD ENTRY", 1.8),
    ("Admin#Pass99", "POSSIBLE PASSWORD ENTRY", 1.5),
    ("this is a very long sentence that was typed extremely quickly for demonstration", "RAPID TYPING ACTIVITY", 4.2),
    ("another rapid typing example with lots of content", "RAPID TYPING ACTIVITY", 3.8),
    ("working on the project", "NORMAL INPUT", 5.1),
    ("email example test", "NORMAL INPUT", 3.9),
    ("7890", "POSSIBLE PIN ENTRY", 1.0),
    ("SecureKey#2024", "POSSIBLE PASSWORD ENTRY", 2.3),
    ("normal workflow continues here", "NORMAL INPUT", 4.8),
]

def generate_logs(num_entries=15):
    """Generate sample log entries"""
    print("🔄 Generating sample keystroke logs...")
    
    # Clear existing log file
    with open(LOG_FILE, "w") as f:
        f.write("")
    
    # Generate entries with timestamps spread over last hour
    start_time = datetime.now() - timedelta(hours=1)
    
    for i in range(num_entries):
        # Pick a random sample or cycle through them
        input_text, classification, duration = SAMPLE_LOGS[i % len(SAMPLE_LOGS)]
        
        # Create timestamp (spread entries over time)
        timestamp = start_time + timedelta(minutes=i * 4)
        timestamp_str = timestamp.strftime("%a %b %d %H:%M:%S %Y")
        
        # Add some variation to duration
        varied_duration = round(duration + random.uniform(-0.5, 0.5), 1)
        
        # Write log entry
        log_entry = f"[{timestamp_str}] [{classification}] [Duration: {varied_duration}s] Input: {input_text}\n"
        
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
        
        print(f"  ✓ [{classification}] {input_text[:30]}...")
        time.sleep(0.1)  # Small delay for visual effect
    
    print(f"\n✅ Generated {num_entries} log entries in {LOG_FILE}")
    print("📊 Now refresh your Streamlit dashboard to see the results!")

if __name__ == "__main__":
    print("=" * 60)
    print(" Sample Keystroke Log Generator")
    print(" For Testing the Streamlit Dashboard")
    print("=" * 60)
    print()
    
    # Ask for number of entries
    try:
        num = input("How many log entries to generate? (default: 15): ").strip()
        num_entries = int(num) if num else 15
    except ValueError:
        num_entries = 15
    
    generate_logs(num_entries)
    
    print("\n" + "=" * 60)
    print(" Open http://localhost:8501 to view the dashboard!")
    print("=" * 60)
