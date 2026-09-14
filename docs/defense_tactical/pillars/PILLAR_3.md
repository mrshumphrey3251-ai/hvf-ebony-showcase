# 👁️ PILLAR 3: UNIVERSAL DRONE COMPUTER VISION & MULTISPECTRAL ANALYSIS
**Document ID:** HDT-OPS-PLR-003
**Classification:** Kinetic Threat Detection / Edge AI

---

## 1. AUTONOMOUS INGEST PIPELINE & RTMP MESH
Humphrey Defense Tactical (HDT) processes live kinetic video directly on the edge node. We do not stream raw optics to the cloud, eliminating latency and securing proprietary troop movements. 

### 1.1 Video Ingest Topology
*Direct kinetic edge processing without cloud latency.*

*   **Layer 1: The Kinetic Edge**
    *   `[SOURCE]` **Autonomous UAV Swarm** transmits encrypted RF telemetry.
    *   `[RECV]` **Local Field Antenna** acts as the localized receiver.
*   **Layer 2: Local Aggregation**
    *   `[INGEST]` **MediaMTX Local Server** captures the raw feed on RTMP Port 1935.
*   **Layer 3: Sovereign Analysis**
    *   `[VISION]` **YOLOv10 Frame Extractor** identifies threats in real-time.
    *   `[VAULT]` **SQLite Threat Vault** logs the coordinates.
    *   `[COMMAND]` **Streamlit Master Console** alerts the Executive Commander.

---

## 2. MULTISPECTRAL SENSOR MATRIX

| Sensor Type | Operational Band | Kinetic Application | Processing Latency |
| :--- | :--- | :--- | :--- |
| **FLIR Thermal** | 7.5 - 13.5 µm | Night-vision organic threat detection | < 45ms |
| **LiDAR** | 905nm | Topographical mapping, canopy penetration | < 60ms |
| **RGB High-Res** | Visible Light | Facial recognition, asset logging | < 30ms |

---

## 3. STANDARD OPERATING PROCEDURES (SOP)

### 3.1 Field Calibration & Focus

1. Deploy UAV swarm on the localized Tailscale mesh network.
2. Verify RTMP stream integrity via local `ffplay`.
3. Initiate Local Computer Vision diagnostic within the Master Console.
4. Set thermal threshold variances based on ambient FOB temperatures.
