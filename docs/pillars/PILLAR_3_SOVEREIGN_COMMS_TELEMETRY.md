# 📡 PILLAR 3: SOVEREIGN COMMUNICATIONS & TELEMETRY MATRIX
**Document ID:** HVF-OPS-PLR-003  
**Classification:** Sovereign Industrial Standard / Encrypted Command Mesh  
**Author:** Jeffery Humphrey, Founder & CEO, Humphrey Virtual Farms  
**Target Systems:** MediaMTX Ingest, Encrypted SQLite Comm Vault, API Endpoints  

---

## 1. ZERO-KNOWLEDGE COMMAND MESH

### 1.1 Secure Internal Messaging Architecture
To prevent local surveillance and secure proprietary field directives, all internal platform communications are cryptographically sealed before touching the disk. The `Sovereign Comms Deck` utilizes military-grade symmetric encryption.

* **Cipher Standard:** Advanced Encryption Standard (AES-128-CBC) combined with SHA-256 HMAC authentication via the `Fernet` specification.
* **Storage Schema (`encrypted_user_comms`):**
  * `sender_username`: Plaintext identifier for routing.
  * `encrypted_payload`: The AES-encrypted binary string of the message content.
  * `timestamp`: Local execution time of the directive.
* **Key Management:** The decryption key is held securely in the application environment (`st.secrets` or local `.env`). Without this key, the SQLite database appears as cryptographic noise, neutralizing physical hardware theft.

---

## 2. DRONE TELEMETRY & MEDIA INGEST (MEDIA MATRIX)

### 2.1 MediaMTX Edge Video Server
Live UAV surveillance and autonomous tractor camera feeds do not route through cloud providers. They stream directly to the local edge node utilizing a bare-metal MediaMTX deployment.

* **Network Ingest Protocols:**
  * **RTMP (Port 1935):** Primary high-bandwidth ingest for DJI and Pixhawk-based drones.
  * **WebRTC (Port 8889):** Ultra-low latency browser playback on the `ebony_console_GREEN.py` UI.
  * **HLS (Port 8888):** Fallback protocol for mobile field terminals.

### 2.2 Subnet Isolation
To prevent external probing, telemetry equipment operates on an isolated `192.168.50.X` subnet, bridging to the Master Console strictly through authenticated Tailscale tunnels. No raw video feed is ever exposed to the public WAN.

---

## 3. ENVIRONMENTAL & OSINT PIPELINES

### 3.1 NOAA NEXRAD Radar Integration
Precision agriculture requires deterministic weather data, not interpolated consumer forecasts. The platform integrates direct API pulls from NOAA NEXRAD stations to overlay raw precipitation dBZ metrics onto the active field map, bypassing third-party weather brokers.

### 3.2 The LinkedIn Engine
For industry dominance and automated digital presence, the system leverages an authorized OAuth pipeline to autonomously synthesize and deploy thought-leadership operations directly from the Master CEO's local instance to the global network.

---

## 4. STANDARD OPERATING PROCEDURES (SOP)

### 4.1 Binding a New UAV to the Media Matrix
1. Connect the UAV ground station to the local isolated Wi-Fi subnet.
2. Configure the drone's RTMP broadcast URL to: `rtmp://[REDACTED_NODE_IP]:1935/live/drone_01`
3. Open the **⬛ Media Matrix** tab on the console.
4. Verify the WebRTC stream renders frame data at >24fps.

### 4.2 Cryptographic Key Rotation Protocol
1. Generate a new `Fernet` symmetric key via standard Python cryptography libraries.
2. Enter the Executive Kinetic PIN (`HVF-OMEGA`) to unlock the database migration script.
3. Decrypt all existing `encrypted_user_comms` with the legacy key, re-encrypt with the new key, and commit to `hvf_memory_vault.db`.

---

## 5. REVISION HISTORY & GOVERNANCE
* **v1.0.0:** Established internal Fernet comms matrix, MediaMTX RTMP ingest paths, and API aggregation pipelines.
* **Approved By:** Jeffery Humphrey, Founder & CEO
* **Enforcement:** Sovereign Master Console Runtime Protocol
