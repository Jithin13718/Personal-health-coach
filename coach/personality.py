def select_personality(adherence: float, intent: str) -> str:
    if intent == "educate":
        return "educational"

    if adherence < 0.3:
        return "supportive"

    if adherence < 0.6:
        return "motivational"

    if adherence >= 0.8:
        return "strict"

    return "neutral"
