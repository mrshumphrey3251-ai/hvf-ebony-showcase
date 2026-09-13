# HVF Developer Onboarding & API Reference
**Classification:** INTERNAL STRICT / HVF GOVERNANCE

## 1. Local Development Setup
1. Clone repository and initialize the secure virtual environment.
2. Launch GLI Microservice: uvicorn src.ai_engine.gli_calc:app --reload
3. Auto-generated OpenAPI/Swagger UI is immediately available at: http://localhost:8000/docs

## 2. Ingesting Dummy Drone Feed
To simulate drone telemetry locally for dashboard testing, execute the adapter:
python src/ingestion/adapters/drone_rgb_adapter.py

## 3. Adding a New Sensor Source
All new IoT/Edge hardware must conform to the JSON-LD schema defined in src/ingestion/schemas/sensor_schema_v1.json. 

*Executive Mandate: New engineers must complete local environment setup and push their first telemetry metric within 30 minutes of onboarding.*
