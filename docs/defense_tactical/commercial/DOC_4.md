# 🤝 DOC 4: OPERATIONAL SLA
**Document ID:** HDT-COM-DOC-004

## 1. SERVICE LEVEL GUARANTEES
* **Inference Latency:** Guaranteed sub-20ms database read/write speeds under high-frequency drone telemetry ingest.
* **Uptime:** Local LLM inference via Ollama is guaranteed to execute without external network calls, ensuring 100% uptime regardless of global internet availability or SATCOM jamming.
* **Data Loss:** Zero byte loss via strict SQLite WAL implementation.