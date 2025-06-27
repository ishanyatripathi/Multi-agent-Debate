# 🧠 Multi-Agent Debate CLI

This project is a command-line based multi-round debate simulation between two AI agents — a **Scientist** and a **Philosopher** — on a user-defined topic. It uses autonomous generation (via GPT) and decision-making logic (LangGraph) to simulate 4 rounds of debate and declare a winner.

---

## 📌 Features

- 🤖 Agent A (Scientist) and Agent B (Philosopher)
- 🧩 4-round back-and-forth debate on any topic
- 🧠 AI-generated replies using GPT-2
- ⚖️ Judge decides winner each round using intelligent logic (sentiment, length)
- 📝 Full memory logging of debate rounds
- ✅ Clean CLI interface, minimal dependencies

---

## 🗂️ Folder Structure

```
task2/
├── nodes/                  # Node logic for agents and judge
│   ├── agent_a_node.py
│   ├── agent_b_node.py
│   ├── judge_node.py
│   └── user_input_node.py
├── utils/                  # Logging and validation utilities
│   ├── logger.py
│   └── validators.py
├── logs/                   # Stores logs of debate
│   └── debate_log.txt
├── main.py                 # CLI entry point
├── structure.txt           # (Optional) explanation or notes
└── .gitignore              # Ignores __pycache__, .pyc, and logs
```

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/debate-cli
cd debate-cli
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

If no `requirements.txt`, use:
```bash
pip install torch transformers langgraph
```

### 3. Run the CLI
```bash
python main.py
```

You'll see:
```
Multi-Agent Debate CLI
Type /exit to quit.
Enter a debate topic:
```

---

## 🧠 Judge Logic

The judge evaluates based on:
- Sentiment score (via DistilBERT)
- Length and clarity
- Keyword presence

---

## 📄 Example Output

```
Enter a debate topic: AI replacing jobs
Judge Decision: Agent A wins round 1
Judge Decision: Agent B wins round 2
Judge Decision: Agent A wins round 3
Judge Decision: Agent B wins round 4

Winner: Agent B
```

---

## 📒 Notes

- You can view the full conversation in `logs/debate_log.txt`.
- The system uses GPT-2 for reply generation, and DistilBERT for judging.
- Meant for educational experimentation and NLP practice.

---
