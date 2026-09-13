# ⚡ PILLAR 2: EBONY NEURAL PROCESSING & PREDICTIVE MEMORY
**Document ID:** HDT-OPS-PLR-002
**Classification:** Cognitive Edge Architecture

## 1. DUAL-ENGINE TACTICAL ARCHITECTURE
Commercial LLMs introduce latency and operational vulnerabilities. Ebony is architected as an air-gapped, zero-hallucination cognitive assistant:
* **Cloud Fast Burst (Online Mode):** High-throughput TLS 1.3 encrypted endpoint for complex reasoning when SATCOM is active.
* **Local Air-Gapped Core (Offline Mode):** Quantized models running directly on bare-metal VRAM via Ollama (Port 11434).

## 2. THIRD BRAIN COGNITIVE CACHE
To eliminate redundant compute cycles during firefights, Ebony implements a local SQLite cache vault. Incoming prompts are hashed (SHA-256). Cache hits return pre-compiled strategic responses in under 15ms at zero token cost.