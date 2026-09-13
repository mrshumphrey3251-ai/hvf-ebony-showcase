# 📡 PILLAR 4: IOT MESH & PERIMETER TELEMETRY
**Document ID:** HDT-OPS-PLR-004
**Classification:** Secure Field Communications

## 1. P2P COMMAND MESH
HDT utilizes an encrypted Tailscale P2P mesh network to link the Master Edge Node to offline field terminals and mobile assault units. This prevents man-in-the-middle attacks and localizes all comms.

## 2. SEISMIC & KINETIC SENSORS
Edge nodes ingest data from perimeter capacitance and seismic sensors, aggregating the telemetry into the local database and flagging anomalies based on deterministic, commander-defined thresholds.