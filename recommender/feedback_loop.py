class FeedbackLoop:
    def __init__(self):
        self.feedback_store = []

    def record(self, user_id: str, recommendation: str, accepted: bool):
        self.feedback_store.append({
            "user_id": user_id,
            "recommendation": recommendation,
            "accepted": accepted
        })

    def adherence_score(self, user_id: str) -> float:
        user_feedback = [
            f for f in self.feedback_store if f["user_id"] == user_id
        ]

        if not user_feedback:
            return 0.0

        accepted = sum(1 for f in user_feedback if f["accepted"])
        return round(accepted / len(user_feedback), 2)
