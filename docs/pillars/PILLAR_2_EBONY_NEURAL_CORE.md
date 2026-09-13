# ⚡ PILLAR 2: EBONY NEURAL PROCESSING & PREDICTIVE MEMORY
**Document ID:** HVF-OPS-PLR-002  
**Classification:** Sovereign Industrial Standard / Cognitive Edge Architecture  
**Author:** Jeffery Humphrey, Founder & CEO, Humphrey Virtual Farms  
**Target Systems:** Bare-Metal Edge Nodes, Local LLM Ingest, Zero-Token Cache  

---

## 1. DUAL-ENGINE ARCHITECTURE & DETERMINISTIC ROUTING

### 1.1 The Pitfalls of Cloud-Only Generative AI
Commercial LLM APIs introduce unacceptable operational vulnerabilities for precision agriculture: non-deterministic outputs, API rate limiting, latency spikes (>2000ms), and critical data leaks caused by transmitting proprietary farm telemetry to remote third-party servers.

### 1.2 The Sovereign Dual-Engine Solution
Ebony is architected as an air-gapped, zero-hallucination cognitive assistant operating across two redundant execution pathways:
1. **Cloud Fast Burst (Online Mode):** Groq LPU endpoint (`openai/gpt-oss-120b`) delivering high-throughput inference with TLS 1.3 encryption for complex reasoning.
2. **Local Air-Gapped Core (Offline Mode):** Quantized `llama3:8b` running directly on bare-metal VRAM via Ollama (Port 11434) with zero external internet dependencies.
3. **Deterministic Constraint:** Temperature is strictly locked to $T = 0.0$ across both engines to ensure 100% reproducible, factual agronomic telemetry without fabricated metrics.

---

## 2. THIRD BRAIN COGNITIVE CACHE & ZERO-TOKEN VAULT

### 2.1 SHA-256 Prompt Hashing Mechanics
To eliminate redundant compute cycles and achieve real-time response speeds, Ebony implements a local SQLite cache vault (`[REDACTED_CACHE_VAULT]`):

$$\text{Query Hash} = \text{SHA-256}(\text{Normalized Prompt Text})$$

* **Execution Workflow:**
  1. Incoming prompt text is stripped of trailing whitespace and lowercase-normalized.
  2. SHA-256 hash is computed in under 1ms.
  3. The local database executes an indexed lookup on `[REDACTED_CACHE_VAULT]`.
  4. **Cache Hit:** Pre-compiled response is served immediately (< 15ms latency) at **0 Tokens** consumed.
  5. **Cache Miss:** The prompt routes to the active neural engine, streams to the UI, and commits to `[REDACTED_CACHE_VAULT]` with an asynchronous background worker.

```
[ User Prompt ] ───> [ SHA-256 Normalizer ] ───> [ Third Brain Vault Query ]
                                                          │
                 ┌────────────────────────────────────────┴────────────────────────────────────────┐
                 ▼                                                                                 ▼
       [ Cache Hit (<15ms) ]                                                             [ Cache Miss ]
        ⚡ Return Stored Response                                                            │
        (0 Tokens Consumed)                                                       ┌────────┴────────┐
                                                                                  ▼                 ▼
                                                                           [ Groq Online ]   [ Ollama Offline ]
                                                                                  │                 │
                                                                                  └────────┬────────┘
                                                                                           ▼
                                                                               [ Commit Hash to Vault ]
```

---

## 3. ASYNCHRONOUS ENTITY EXTRACTION & LONG-TERM MEMORY

### 3.1 Memory Core Schema
Ebony maintains persistent conversational memory across application restarts through the `[REDACTED_ENTITY_CORE]` table:

* **Extracted Entity Types:**
  * `FIELD_PARCEL`: Parcel identifiers, acreage boundaries, soil classification markers.
  * `CROP_STRAIN`: Plant genetics, hybrid serial numbers, seeding dates.
  * `SENSOR_NODE`: Hardware MAC addresses, capacitance probe depths, battery voltage status.
  * `OPERATIONAL_EVENT`: Spray dates, canopy indices (GLI), irrigation valve trigger histories.

### 3.2 Context Injection Pipeline
Prior to inference, the engine queries recent entity markers and injects a distilled system context payload directly into the active prompt window, ensuring the assistant retains full farm situational awareness without context bloat.

---

## 4. STANDARD OPERATING PROCEDURES (SOP)

### 4.1 Verifying the Local Ollama Engine
1. Open a PowerShell terminal on the Master Workstation.
2. Check local model availability:
   `ollama list`
3. Test local inference independently:
   `ollama run llama3:8b "Summarize precision agriculture VWC thresholds."`
4. Ensure port 11434 is open for local loopback connections (`[REDACTED_NODE_IP]:11434`).

### 4.2 Auditing the Third Brain Vault
1. In the event of schema migration or system cache inspection, open the SQLite CLI:
   `sqlite3 [REDACTED_VAULT_DB]`
2. View total cached zero-token entries:
   `SELECT COUNT(*) FROM [REDACTED_CACHE_VAULT];`
3. Audit recent cached queries:
   `SELECT query_hash, SUBSTR(response_text, 1, 60), created_at FROM [REDACTED_CACHE_VAULT] ORDER BY id DESC LIMIT 5;`

---

## 5. REVISION HISTORY & GOVERNANCE
* **v1.0.0 (Initial Commercial Standard):** Implemented dual-engine Groq/Ollama routing, SHA-256 zero-token caching, and persistent entity memory.
* **Approved By:** Jeffery Humphrey, Founder & CEO
* **Enforcement:** Sovereign Master Console Runtime Protocol
