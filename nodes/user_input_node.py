# nodes/user_input_node.py

class UserInputNode:
    def __call__(self, state) -> dict:
        topic = state.topic.strip()
        if not topic:
            raise ValueError("No debate topic provided.")
        return {
            "topic": topic,
            "round_number": 1,
            "memory": [],
            "log": [f"🎯 Topic: {topic}"]
        }
