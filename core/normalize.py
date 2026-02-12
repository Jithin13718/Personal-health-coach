from collections import defaultdict
from datetime import datetime

def normalize_records(user_id: str, records: list) -> dict:
    """
    Input: list of ingestion records
    Output: unified user_metrics dict
    """

    normalized = {
        "user_id": user_id,
        "date": None,
        "source": set(),
        "metrics": defaultdict(float)
    }

    for record in records:
        normalized["source"].add(record.get("source"))

        # Handle date
        if "date" in record:
            normalized["date"] = record["date"]
        elif "timestamp" in record:
            normalized["date"] = record["timestamp"][:10]

        # Metric-based records
        if "metric" in record:
            normalized["metrics"][record["metric"]] += record["value"]

        # Meal records
        if record.get("type") == "meal":
            normalized["metrics"]["calories_in"] += record["calories"]
            for macro, value in record["macros"].items():
                normalized["metrics"][macro] += value

        # Workout records
        if record.get("type") == "workout":
            normalized["metrics"]["calories_out"] += record["calories_burned"]

    normalized["source"] = list(normalized["source"])
    normalized["metrics"] = dict(normalized["metrics"])

    return normalized
