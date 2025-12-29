# 🧠 AI-Enhanced Keystroke Logging for Cybersecurity Awareness

> **Educational Project**: This project demonstrates how keystroke patterns can be analyzed to infer user behavior WITHOUT stealing sensitive data. It serves as a cybersecurity awareness tool to help defenders design better detection and prevention systems.

## 🎯 Project Overview

This system consists of two components:

1. **AI Keylogger Agent** - A local monitoring agent that captures and classifies keystroke patterns
2. **Streamlit Dashboard** - A visualization interface that analyzes and displays behavior patterns

### Architecture Flow

```
AI Keylogger Agent (local, consent-based)
        ↓
keylog_ai.txt (log file)
        ↓
Streamlit Dashboard (awareness + analysis)
```

## 🛡️ Ethical Framework

**Instead of capturing sensitive data, this agent demonstrates how attackers infer user behavior patterns, helping defenders design better detection and prevention systems.**

### Key Principles

- ✅ **Local-only logging** - No network transmission
- ✅ **Pattern inference** - Analyzes behavior, not content
- ✅ **Educational purpose** - Raises cybersecurity awareness
- ✅ **Transparent operation** - Clear indicators when running
- ❌ **No data exfiltration** - Everything stays on your machine

## 🚀 Features

### AI Agent Capabilities

- **Autonomous input monitoring** - Continuous keystroke capture
- **Context memory** - Session-based buffering
- **Pattern inference** - Rule-based classification engine
- **Decision output** - Real-time risk assessment
- **Continuous operation** - Agent-based architecture

### Pattern Detection

The agent classifies inputs into categories:

- 🔢 **PIN-like entries** - Numeric patterns suggesting authentication
- 🔐 **Password-like entries** - Complex patterns with letters, symbols, and digits
- ⚡ **Rapid typing** - High-speed input suggesting normal workflow
- ✏️ **Normal input** - Standard typing behavior

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/keystroke-logging-demonstration.git
cd keystroke-logging-demonstration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Step 1: Run the AI Keylogger Agent

```bash
python ai_keylogger_agent.py
```

The agent will start monitoring keystrokes and logging patterns to `keylog_ai.txt`.

**Controls:**
- Type normally to generate sample data
- Press `ENTER` to complete an input session
- Press `CTRL + C` to stop the agent

### Step 2: Launch the Streamlit Dashboard

In a separate terminal:

```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 📊 Dashboard Features

### Metrics Overview
- Total input events captured
- PIN-like event detection count
- Password-like event detection count
- Rapid typing event detection count

### Visual Log Analysis
- Color-coded event display
- Reverse chronological ordering
- Pattern classification labels
- Timestamp tracking

### Cybersecurity Insights
- Educational explanations
- Defense strategy recommendations
- Awareness training guidance

## 🔍 How It Works

### Pattern Analysis Algorithm

The agent uses rule-based heuristics to classify keystroke patterns:

```python
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
```

### Agent Architecture

The system operates as an **autonomous agent** with:

1. **Perception** - Keystroke event capture via `pynput`
2. **Memory** - Session buffer management
3. **Reasoning** - Pattern classification logic
4. **Action** - Log file writing with classifications

## 📸 Sample Output

```
[Sun Dec 29 21:11:10] [NORMAL INPUT] [Duration: 6.2s] Input: hello this is demo
[Sun Dec 29 21:11:22] [POSSIBLE PIN ENTRY] [Duration: 1.4s] Input: 4829
[Sun Dec 29 21:11:40] [POSSIBLE PASSWORD ENTRY] [Duration: 2.1s] Input: pass@123
```

## 🎓 Educational Use Cases

### For Students
- Understanding keystroke logging threats
- Learning behavior-based security
- Exploring AI agent architectures
- Cybersecurity awareness training

### For Defenders
- Endpoint monitoring strategies
- Behavior-based detection systems
- User activity analysis
- Threat modeling exercises

### For Researchers
- Keystroke dynamics research
- Pattern recognition studies
- Privacy-preserving analytics
- Educational tool development

## ⚠️ Important Disclaimers

### Legal Notice
This project is for **educational purposes only**. Unauthorized keystroke logging is illegal in most jurisdictions. Always:
- Obtain explicit consent before monitoring
- Use only on systems you own or have permission to test
- Comply with local laws and regulations
- Never deploy on production systems without authorization

### Ethical Guidelines
- **Never** use this tool to capture sensitive information
- **Always** disclose when monitoring is active
- **Only** operate in controlled, educational environments
- **Respect** user privacy and data protection laws

## 🛠️ Technical Stack

- **Python** - Core language
- **pynput** - Keyboard event capture
- **Streamlit** - Dashboard framework
- **pandas** - Data manipulation (optional)

## 📁 Project Structure

```
keystroke-logging-demonstration/
│
├── ai_keylogger_agent.py      # Main monitoring agent
├── app.py                      # Streamlit dashboard
├── keylog_ai.txt               # Generated log file (created at runtime)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── screenshots/                # Demo screenshots (optional)
```

## 🤝 Contributing

This is an educational project. If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Add educational enhancements
4. Submit a pull request

**Contribution Guidelines:**
- Maintain ethical focus
- Enhance educational value
- Improve privacy protections
- Add security awareness features

## 📚 Further Reading

### Cybersecurity Resources
- NIST Cybersecurity Framework
- OWASP Security Guidelines
- ISO 27001 Information Security Standards

### Research Papers
- Keystroke Dynamics in User Authentication
- Behavior-Based Intrusion Detection Systems
- Privacy-Preserving Activity Monitoring

## 📝 License

This project is released under the MIT License for educational purposes only.

## 👨‍💻 Author

Created as an educational cybersecurity awareness project.

---

**Remember**: The goal is not to steal data, but to understand how attackers think so we can build better defenses.

🛡️ **Defend. Detect. Develop.**
