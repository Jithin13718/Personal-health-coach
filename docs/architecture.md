# Health Coach Agent – Architecture Overview

## High-Level Flow
Ingestion → Core Processing → Recommendation Engine → Coaching Layer → Integration


---

## Layer Responsibilities

### 1. Ingestion
- Collects raw health data from:
  - Wearables (Fitbit, Apple Health)
  - Manual user input
- No business logic
- Outputs normalized records

### 2. Core
- Normalizes raw data into a unified schema
- Compresses historical data into trends
- Produces deterministic, testable outputs

### 3. Recommender
- Rule-based logic for immediate value
- ML-ready design for personalization
- Feedback loop to measure adherence

### 4. Coach
- Detects user intent
- Generates empathetic, actionable responses
- Combines recommendations + tone

### 5. Integration
- Subscription, billing, APIs
- External services and dashboards

---

## Design Principles
- Modular and replaceable components
- Clear data contracts between layers
- Safe defaults (non-medical advice)
- ML optional, rules first
