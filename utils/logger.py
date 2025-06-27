import re
from datetime import datetime

# Safely remove emojis and unsupported characters
def remove_emojis(text):
    if isinstance(text, (int, float)):
        return str(text)
    if text is None:
        return ""
    return re.sub(r'[^\w\s.,:;\'"!?()\[\]{}<>@#%^&*+=\-\\/|]', '', str(text))

def log_state(state):
    try:
        with open("logs/debate_log.txt", "a", encoding="utf-8") as f:
            f.write(f"\n=== Debate Log: {datetime.now()} ===\n")

            # Works with dataclass or dict-like state
            state_dict = state.__dict__ if hasattr(state, "__dict__") else dict(state)

            for key, value in state_dict.items():
                line = f"{key}: {remove_emojis(value)}\n"
                f.write(line)

            f.write("=== End ===\n")
    except Exception as e:
        print(f"[ERROR] Failed to write log: {e}")
