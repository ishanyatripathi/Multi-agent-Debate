# utils/validators.py

def validate_topic(topic: str) -> bool:
    if not topic or not isinstance(topic, str) or len(topic.strip()) < 5:
        return False
    return True
