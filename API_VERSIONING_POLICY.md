# SOVEREIGN API VERSIONING & SUNSET POLICY
## Enterprise Integration Stability Standard

Humphrey Virtual Farms engineers data pipelines for massive-scale agricultural OEMs. We do not introduce breaking changes to live production endpoints.

### 1. Versioning Architecture
All API endpoints are explicitly versioned in the URI path (e.g., https://api.humphreyvirtualfarms.com/v2/telemetry). We employ non-breaking additions (new fields) within active versions, but any structural schema change forces a version increment.

### 2. The 12-Month Sunset Mandate
When a new API version is released (e.g., 2), the prior version (1) enters a locked, deprecated state. 
* The legacy endpoint remains fully operational for exactly **12 months**.
* A standard HTTP Warning: 299 header is injected into all deprecated responses to alert integrators.
* After 12 months, the legacy endpoint is severed.

We provide predictable, military-grade stability for our ecosystem partners.
