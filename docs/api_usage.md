# API Usage Guide

This project is designed to be API-agnostic.
You can expose functionality using REST, GraphQL, or gRPC.

---

## Example: Daily Coaching Flow

### 1. Ingest Data
```python
records = [
    fitbit_adapter.get_daily_steps(),
    manual_input.log_meal(...)
]
normalized = normalize_records(user_id, records)
weekly_trends = compress_history(history_data)
recs = generate_rule_based_recommendations(normalized["metrics"])
intent = dialogue_manager.detect_intent(user_message)
response = dialogue_manager.generate_response(intent, recs)
