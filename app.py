import streamlit as st
import pandas as pd
import os
import re

st.set_page_config(page_title="AI Keystroke Awareness Dashboard", layout="wide")

st.title("🧠 AI-Enhanced Keystroke Logging for Cybersecurity Awareness")
st.markdown(
    """
This dashboard visualizes **keystroke behavior patterns** collected in a **controlled,
educational environment** to demonstrate how attackers *infer sensitive activity*
and how defenders can detect risks.

⚠️ No keystrokes are captured here.  
📂 This app only **reads a local log file**.
"""
)

LOG_FILE = "keylog_ai.txt"

# ---------------------------
# Load Log Data
# ---------------------------
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as f:
        return f.readlines()

logs = load_logs()

# ---------------------------
# Summary Metrics
# ---------------------------
st.subheader("📊 Activity Summary")

total_entries = len(logs)
pin_events = sum("POSSIBLE PIN" in l for l in logs)
password_events = sum("POSSIBLE PASSWORD" in l for l in logs)
rapid_events = sum("RAPID TYPING" in l for l in logs)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Inputs", total_entries)
col2.metric("PIN-Like Events", pin_events)
col3.metric("Password-Like Events", password_events)
col4.metric("Rapid Typing Events", rapid_events)

# ---------------------------
# Detailed Log Viewer
# ---------------------------
st.subheader("📄 Logged Events")

if logs:
    for log in logs[::-1]:
        if "POSSIBLE PASSWORD" in log:
            st.error(log)
        elif "POSSIBLE PIN" in log:
            st.warning(log)
        elif "RAPID TYPING" in log:
            st.info(log)
        else:
            st.write(log)
else:
    st.info("No log data found. Run the AI keylogger agent first.")

# ---------------------------
# Awareness Section
# ---------------------------
st.subheader("🛡️ Cybersecurity Insight")

st.markdown(
    """
### What This Demonstrates
- Attackers **do not need exact passwords**
- **Behavior patterns** are enough to infer risk
- Rapid input + symbols + digits = high-risk activity

### Defensive Learning
✔ Endpoint monitoring  
✔ Behavior-based detection  
✔ User awareness training  

This project demonstrates **how keylogging threats work**
so better **prevention systems** can be designed.
"""
)

st.markdown("---")
st.caption("Educational Project • No Data Exfiltration • Local Analysis Only")
