import random
import yaml
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

class DialogueManager:
    def __init__(self):
        with open(BASE_DIR / "intents.yaml", "r") as f:
            self.intents_config = yaml.safe_load(f)

        with open(BASE_DIR / "response_templates.json", "r") as f:
            self.templates = json.load(f)

    def detect_intent(self, user_message: str) -> str:
        message = user_message.lower()

        for intent, keywords in self.intents_config["keywords"].items():
            if any(word in message for word in keywords):
                return intent

        return "motivate"

    def generate_response(self, intent: str, recommendations: list = None) -> str:
        base_response = random.choice(self.templates.get(intent, []))

        if recommendations:
            advice = " ".join(recommendations[:1])
            return f"{base_response} {advice}"

        return base_response
