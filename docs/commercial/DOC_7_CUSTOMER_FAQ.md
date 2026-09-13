# ℹ️ DOC 7: CUSTOMER-FACING FAQ
**Document ID:** HVF-COM-DOC-007  
**Classification:** Commercial Operations / Client Relations  
**Author:** Jeffery Humphrey, Founder & CEO, Humphrey Virtual Farms  
**Target Systems:** Prospective Clients, Procurement Teams, Integration Partners  

---

## 1. GENERAL INFRASTRUCTURE

### Q: Why does HVF use local edge-computing instead of AWS or Azure like other AgTech platforms?
**A:** Precision agriculture cannot wait on latency, and it cannot halt when rural internet degrades. By deploying the Ebony Neural Core on bare-metal hardware directly at your farm, we guarantee sub-15ms inference speeds and absolute immunity to global internet outages. 

### Q: Do I need to buy a specific brand of drone or tractor?
**A:** No. The Sovereign Edge architecture is hardware-agnostic. As long as the drone broadcasts a standard RTMP/RTSP video feed and the tractor accepts standard telemetry protocols, the Master Edge Node can ingest and orchestrate it.

---

## 2. DATA OWNERSHIP & SECURITY

### Q: Does Humphrey Virtual Farms sell or aggregate my crop data?
**A:** Absolutely not. We operate a zero-telemetry architecture. Your data never leaves your physical property. All neural processing is done locally, and your `hvf_memory_vault.db` is yours alone.

### Q: How secure is the data stored on the farm?
**A:** Military-grade. All data at rest is encrypted using AES-128-CBC (`Fernet`). Furthermore, access is governed by a strict 3-Tier Role-Based Access Control (RBAC) system. Without the cryptographic keys held by the site CEO, the physical drives are unreadable even if stolen.

---

## 3. KINETIC FALLBACKS & OPERATIONS

### Q: What happens if the internet goes completely down during a storm?
**A:** Operations continue seamlessly. The edge node communicates with local LoRaWAN soil probes and UAV hangars over an isolated `192.168.50.X` subnet. The system caches NOAA weather data and uses its offline LLM to maintain kinetic safety interlocks without needing an external WAN connection.

### Q: Can someone hack my irrigation valves or drones over the internet?
**A:** No. The Master Edge Node acts as an air-gapped fortress. The only external ingress point is an end-to-end encrypted Tailscale mesh tunnel, which requires cryptographic authentication from the site CEO to establish a connection.
