# JudgeNode.py

class JudgeNode:
    def __init__(self, device="cpu"):
        from transformers import pipeline
        self.judge_model = pipeline("sentiment-analysis", device=0 if device == "cuda" else -1)

    def __call__(self, state):
        a = state.agent_a_reply or ""
        b = state.agent_b_reply or ""

        score_a = self._score_argument(a)
        score_b = self._score_argument(b)

        if score_a > score_b:
            winner = "Agent A"
        elif score_b > score_a:
            winner = "Agent B"
        else:
            winner = "Draw"

        print(f"\n Judge Decision: {winner} wins round {state.round_number}.")

        # Save decision and update round
        state.winner = winner
        state.round_number += 1  # ✅ This is critical

        return state

    def _score_argument(self, text):
        sentiment = self.judge_model(text.strip().split("\n")[0])[0]
        confidence = sentiment['score']
        length_score = min(len(text.split()), 100) / 100  # cap long texts
        return confidence + length_score
