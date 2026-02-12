from ingestion.manual_input import ManualInput
from ingestion.apple_health_adapter import AppleHealthAdapter

from core.normalize import normalize_records
from core.compress import compress_history

from recommender.rules_engine import generate_rule_based_recommendations

from coach.dialogue_manager import DialogueManager

from utils.logger import get_logger

logger = get_logger("health_coach")

def run_agent():
    user_id = "user_001"

    # ---------------- Ingestion ----------------
    manual = ManualInput()
    apple = AppleHealthAdapter()

    records = []

    records.append(
        manual.log_meal(
            calories=420,
            protein=25,
            carbs=45,
            fat=12
        )
    )

    records.extend(
        apple.ingest_payload({
            "date": "2026-02-12",
            "steps": 3800,
            "sleep_hours": 6.2
        })
    )

    logger.info("Data ingested")

    # ---------------- Core ----------------
    normalized = normalize_records(user_id, records)
    logger.info(f"Normalized data: {normalized}")

    history = [normalized]  # extend later with past days
    trends = compress_history(history)

    # ---------------- Recommender ----------------
    recommendations = generate_rule_based_recommendations(
        normalized["metrics"]
    )

    # ---------------- Coach ----------------
    coach = DialogueManager()

    user_message = "I feel tired today"
    intent = coach.detect_intent(user_message)

    response = coach.generate_response(intent, recommendations)

    print("\n🤖 Health Coach Response:")
    print(response)


if __name__ == "__main__":
    run_agent()
