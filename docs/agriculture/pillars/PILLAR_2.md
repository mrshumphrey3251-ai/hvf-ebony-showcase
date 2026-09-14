# ⚡ PILLAR 2: EBONY NEURAL PROCESSING & PREDICTIVE MEMORY

**Document ID:** HVF-OPS-PLR-002

**Classification:** Sovereign Industrial Standard / Cognitive Edge Architecture

**Author:** Jeffery Humphrey, Founder & CEO

---

## 1. DUAL-ENGINE ARCHITECTURE & DETERMINISTIC ROUTING

### 1.1 The Pitfalls of Cloud-Only Generative AI
Commercial LLM APIs introduce unacceptable operational vulnerabilities for precision agriculture: non-deterministic outputs, API rate limiting, latency spikes, and critical data leaks.

### 1.2 The Sovereign Dual-Engine Solution
Ebony is architected as an air-gapped, zero-hallucination cognitive assistant operating across two redundant execution pathways:
*   **Cloud Fast Burst (Online Mode):** Groq LPU endpoint delivering high-throughput inference with TLS 1.3 encryption for complex reasoning.
*   **Local Air-Gapped Core (Offline Mode):** Quantized `llama3:8b` running directly on bare-metal VRAM via Ollama (Port 11434).

**Deterministic Constraint:** Temperature is strictly locked across both engines to ensure 100% reproducible, factual agronomic telemetry.## 2. THIRD BRAIN COGNITIVE CACHE & ZERO-TOKEN VAULT

### 2.1 SHA-256 Prompt Hashing Mechanics
To eliminate redundant compute cycles and achieve real-time response speeds, Ebony implements a local SQLite cache vault:
