from datetime import datetime

class ManualInput:
    def log_meal(self, calories: int, protein: float, carbs: float, fat: float) -> dict:
        return {
            "source": "manual",
            "timestamp": datetime.utcnow().isoformat(),
            "type": "meal",
            "calories": calories,
            "macros": {
                "protein": protein,
                "carbs": carbs,
                "fat": fat
            }
        }

    def log_workout(self, workout_type: str, duration_min: int, calories_burned: int) -> dict:
        return {
            "source": "manual",
            "timestamp": datetime.utcnow().isoformat(),
            "type": "workout",
            "workout_type": workout_type,
            "duration_min": duration_min,
            "calories_burned": calories_burned
        }
