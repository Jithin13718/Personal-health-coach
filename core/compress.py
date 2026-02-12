def compress_history(history: list, window: int = 7) -> dict:
    """
    Input: list of daily normalized metrics (ordered by date)
    Output: compressed trend data
    """

    if not history:
        return {}

    compressed = {}
    metric_keys = history[0]["metrics"].keys()

    for key in metric_keys:
        values = [day["metrics"].get(key, 0) for day in history[-window:]]

        compressed[key] = {
            "avg": round(sum(values) / len(values), 2),
            "min": min(values),
            "max": max(values)
        }

    return compressed
