# ⚡ PILLAR 2: EBONY NEURAL PROCESSING & PREDICTIVE MEMORY
**Document ID:** HDT-OPS-PLR-002
**Classification:** Sovereign Industrial Standard / Cognitive Edge Architecture

---

## 1. DUAL-ENGINE ARCHITECTURE & DETERMINISTIC ROUTING

### 1.1 The Sovereign Dual-Engine Solution
Ebony is architected as an air-gapped, zero-hallucination cognitive assistant operating across two redundant execution pathways:

* **Cloud Fast Burst (Online Mode):** Low-latency Groq LPU endpoint delivering high-throughput inference with TLS 1.3 encryption when SATCOM is available.
* **Local Air-Gapped Core (Offline Mode):** Quantized `llama3:8b` running directly on bare-metal VRAM via Ollama (Port 11434) with zero external internet dependencies.
* **Deterministic Constraint:** Temperature is strictly locked to `T=0.0` across both engines to ensure 100% reproducible, factual threat telemetry.

---

## 2. THIRD BRAIN COGNITIVE CACHE & ZERO-TOKEN VAULT

### 2.1 SHA-256 Prompt Hashing Mechanics
To eliminate redundant compute cycles during firefights, Ebony implements a local SQLite cache vault:

`Query Hash = SHA-256(Normalized Prompt Text)`

**Execution Workflow:**

1. Incoming prompt text is lowercase-normalized.
2. SHA-256 hash is computed in under 1ms.
3. Database executes an indexed lookup on the Vault.
4. **Cache Hit:** Pre-compiled response is served immediately (< 15ms latency) at 0 Tokens.
5. **Cache Miss:** Prompt routes to the active neural engine, streams to UI, and commits to Vault.

### 2.2 Local Air-Gapped Cache Topology
*Data routes intelligently to prevent redundant GPU cycles.*

*   **Phase 1: Input & Normalization**
    *   `[INPUT]` Commander Prompt is injected into the interface.
    *   `[HASH]` SHA-256 Normalizer generates a cryptographic signature.
*   **Phase 2: The SQLite Vault Fork**
    *   `[CACHE HIT]` Match found: System returns stored response in <15ms at 0 Tokens.
    *   `[CACHE MISS]` No match: Prompt is routed to the inference engine.
*   **Phase 3: Generation & Memory Commit**
    *   `[ONLINE]` Groq API processes via SATCOM (if available).
    *   `[OFFLINE]` Ollama processes on bare-metal RTX hardware.
    *   `[COMMIT]` The generated response and hash are written permanently to the SQLite Vault.
