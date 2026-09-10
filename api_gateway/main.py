from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Sentinel Ultra API Gateway", description="Sanitized AI Routing Node")

@app.get("/")
def read_root():
    return {"status": "ONLINE", "system": "EBONY_SPEC"}

@app.post("/mission/flight-plan")
def inject_flight_plan(payload: dict):
    # Primary endpoint for the Dart/Flutter UI to inject flight plans. [PUBLIC SPEC]
    return {"status": "SUCCESS"}
