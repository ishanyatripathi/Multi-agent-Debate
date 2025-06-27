from langgraph.graph import StateGraph, END
from dataclasses import dataclass, field
from nodes.user_input_node import UserInputNode
from nodes.agent_a_node import AgentANode
from nodes.agent_b_node import AgentBNode
from nodes.judge_node import JudgeNode
from utils.logger import log_state
from utils.validators import validate_topic
import torch

# ⚙️ Device setup
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Device set to use {device}")

# 📦 State schema
@dataclass
class DebateState:
    topic: str
    round_number: int = 1
    memory: list = field(default_factory=list)
    agent_a_reply: str = None
    agent_b_reply: str = None
    winner: str = None
    log: list = field(default_factory=list)

# 🧠 Conditional routing logic
def continue_or_end(state: DebateState):
    print(f"Round {state.round_number}")
    if state.round_number < 5:
        return "agent_a"
    return END

# 🧱 Graph setup
builder = StateGraph(DebateState)

# 🧩 Nodes
user_input = UserInputNode()
agent_a = AgentANode(device=device)
agent_b = AgentBNode(device=device)
judge = JudgeNode(device=device)

# ➕ Add nodes
builder.add_node("user_input", user_input)
builder.add_node("agent_a", agent_a)
builder.add_node("agent_b", agent_b)
builder.add_node("judge", judge)

# 🔁 Edges
builder.set_entry_point("user_input")
builder.add_edge("user_input", "agent_a")
builder.add_edge("agent_a", "agent_b")
builder.add_edge("agent_b", "judge")
builder.add_conditional_edges("judge", continue_or_end)

# ✅ Compile
graph = builder.compile()

# 6. CLI Interface
if __name__ == "__main__":
    print("Multi-Agent Debate CLI")
    print("Type /exit to quit.\n")

    while True:
        topic = input("Enter a debate topic: ").strip()
        if topic.lower() == "/exit":
            print("Exiting.")
            break

        if not validate_topic(topic):
            print("Invalid topic. Please enter at least 5 characters.")
            continue

        # Invoke the graph
        result = graph.invoke({"topic": topic})

        # Extract actual state object from AddableValuesDict
        state = DebateState(**result)

        print("\n Debate Log:")
        for item in state.memory:
            print(item)

        print(f"\n Final Winner (based on last round): {state.winner}\n")

        log_state(state)
