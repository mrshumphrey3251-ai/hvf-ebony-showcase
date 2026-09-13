# HVF SOC 2 Type II & ISO 27001 Control Matrix
**Classification:** INTERNAL STRICT / HVF GOVERNANCE

## Common Criteria (Security, Availability, Confidentiality)
* **CC6.1 (Logical Access):** Enforced via src/security/rbac_middleware.py. All API endpoints require cryptographic JWT validation.
* **CC7.1 (System Monitoring):** Locust load-testing and Prometheus/Grafana infrastructure log all ingestion latencies.
* **CC8.1 (Change Management):** Enforced via automated CI/CD pipeline (.github/workflows/model_ops_cicd.yml). Zero code reaches production without passing the automated pytest suite.

*Business Associate Agreement (BAA) templates for HIPAA data handling are located in the encrypted HR vault.*
