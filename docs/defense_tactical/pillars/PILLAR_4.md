# 📡 PILLAR 4: IOT MESH & PERIMETER TELEMETRY
**Document ID:** HDT-OPS-PLR-004
**Classification:** Secure Field Communications / Perimeter Defense

## 1. ENCRYPTED P2P COMMAND MESH
HDT utilizes a zero-trust, WireGuard-backed Tailscale P2P mesh network. This isolates the Master Edge Node, offline field terminals, drones, and mobile assault units into a cryptographically sealed subnet. It prevents man-in-the-middle attacks, RF jamming interception, and localized comms loss.

## 2. SEISMIC & CAPACITANCE SENSOR ARRAYS
Perimeter defense relies on deterministic, hardwired telemetry rather than cloud-based predictive algorithms. 

| Telemetry Vector | Sensor Hardware | Alert Threshold | Action Trigger |
| :--- | :--- | :--- | :--- |
| **Seismic Vibration** | Subterranean Geophones | > 4.2 Richter equivalent (Localized) | Drone Swarm Scramble |
| **Capacitance** | Perimeter Fence Relays | < 2.0V Voltage Drop | Kinetic Override / Alarm |
| **Acoustic** | Triangulated Microphones | Decibel spike matching ballistic profiles | Auto-Log to SQLite Vault |

## 3. STANDARD OPERATING PROCEDURES (SOP)
### 3.1 Node Integration & Provisioning
1. Physically wire the new sensor node to the localized PoE (Power over Ethernet) switch.
2. Authenticate the node via the Executive PIN in the Master Console.
3. Verify the node appears in the `[REDACTED_TELEMETRY]` SQLite table via the Python Sandbox.