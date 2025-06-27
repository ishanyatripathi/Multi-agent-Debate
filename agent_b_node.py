# nodes/agent_b_node.py

from transformers import pipeline, set_seed

class AgentBNode:
    def __init__(self, device="cpu"):
        print("Device set to", device)
        self.generator = pipeline("text-generation", model="distilgpt2", device=0 if device == "cuda" else -1)
        set_seed(42)

    def __call__(self, state) -> dict:
        topic = state.topic
        round_number = state.round_number
        memory = state.memory or []

        prompt = f"As a Philosopher in round {round_number}, I believe that '{topic}' must be examined from a logical perspective:"
        output = self.generator(prompt, max_new_tokens=60, do_sample=True, top_k=50, top_p=0.95)[0]["generated_text"]

        reply = output.strip().split("\n")[0]
        memory.append(f"Philosopher (Round {round_number}): {reply}")

        return {
            "agent_b_reply": reply,
            "memory": memory
        }
