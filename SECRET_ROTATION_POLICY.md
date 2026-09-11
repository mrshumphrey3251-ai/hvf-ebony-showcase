# SERVICE-TO-SERVICE SECRET ROTATION POLICY
## Zero-Trust Cryptographic Lifecycle Standard

Humphrey Virtual Farms enforces strict zero-trust operational security across all distributed microservices, edge ingestion gateways, and telemetry pipelines.

### 1. The 30-Day Rotation Lifecycle
All service-to-service authentication tokens and shared HMAC secrets are subject to automated rotation every 30 days. No static, long-lived credentials exist within the sovereign matrix.

### 2. Zero-Downtime Dual-Key Grace Period
To guarantee zero dropped telemetry frames across remote edge nodes during key transitions:
* **Active Key:** Authorizes all newly dispatched requests and telemetry payloads.
* **Grace Key:** The immediate prior key remains valid in a grace state to allow in-flight requests and intermittent edge nodes to authenticate without interruption.
* **Purge Threshold:** Upon subsequent rotation, stale grace credentials are permanently revoked.
