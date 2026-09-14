# 🤝 DOC 4: OPERATIONAL SLA & METRICS
**Document ID:** HDT-COM-DOC-004

---

## 1. SERVICE LEVEL GUARANTEES

| Metric | Target | Hard Limit |
| :--- | :--- | :--- |
| **Local Cache Inference** | < 15ms | < 30ms |
| **Offline LLM Gen** | ~ 45 tokens/sec | > 25 tokens/sec |
| **Sensor Telemetry Write** | < 5ms | < 10ms |
| **Uptime (Air-Gapped)** | 100% | 99.999% |

*Data Loss Guarantee:* Zero byte loss via strict SQLite WAL implementation and atomic commits.
