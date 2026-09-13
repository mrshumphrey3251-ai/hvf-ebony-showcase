# 🌾 PILLAR 4: IOT SOIL TELEMETRY & DIELECTRIC CAPACITANCE
**Document ID:** HVF-OPS-PLR-004-IOT  
**Classification:** Sovereign Industrial Standard / Sub-Surface Telemetry  
**Author:** Jeffery Humphrey, Founder & CEO, Humphrey Virtual Farms  
**Target Systems:** LoRaWAN Edge Gateways, Subterranean Capacitance Probes, Local SQLite Vault  

---

## 1. SOVEREIGN IOT TOPOLOGY

### 1.1 The Vulnerability of Commercial IoT Brokers
Standard precision agriculture relies on AWS IoT Core or Azure IoT Hub to aggregate soil moisture data. This exposes the exact hydration and nutrient profiles of our soil to corporate aggregation. Humphrey Virtual Farms intercepts all probe data locally.

### 1.2 Isolated LoRaWAN Ingestion
1. **Sensors:** Sub-surface dielectric probes transmit via encrypted LoRaWAN (915 MHz).
2. **Edge Gateway:** A local LoRaWAN gateway receives the packets and forwards them exclusively to the `192.168.50.X` isolated subnet.
3. **Ingestion Engine:** A local MQTT broker intercepts the packets, decodes the payload, and writes the raw telemetry directly into `hvf_memory_vault.db`.

---

## 2. DIELECTRIC CAPACITANCE MATHEMATICS

### 2.1 Volumetric Water Content (VWC) Calculation
Raw sensor data returns apparent dielectric permittivity ($\epsilon$). The Ebony engine dynamically converts this to accurate Volumetric Water Content ($\theta$) using the Topp Equation before triggering autonomous irrigation.

```latex
\theta = -5.3 \times 10^{-2} + 2.92 \times 10^{-2}\epsilon - 5.5 \times 10^{-4}\epsilon^2 + 4.3 \times 10^{-6}\epsilon^3
```

### 2.2 Neural Threshold Integration
Ebony's active LLM context window is continuously fed these calculated VWC percentages. If $\theta$ drops below the designated threshold for a specific crop strain, the engine evaluates upcoming NEXRAD precipitation data before authorizing a valve release via the Kinetic Sector Vault.

---

## 3. ASSET MAPPING & DATABASE INTEGRATION

### 3.1 Hardware Registration
Every physical sensor must be registered in the system. The hardware's MAC address is cryptographically bound to its physical GPS coordinates and field sector in the local vault. Unregistered MAC addresses pinging the MQTT broker are automatically blacklisted and dropped.

---

## 4. STANDARD OPERATING PROCEDURES (SOP)

### 4.1 Provisioning a New Subterranean Probe
1. Obtain the DevEUI, AppEUI, and AppKey for the new probe.
2. Access the Master Console natively.
3. Enter the cryptographic keys into the **⚙️ Empire Config** module to bind the sensor to the local LoRa network server.
4. Physically install the probe at the designated GPS coordinates.
5. Verify initial payload ingestion in `hvf_memory_vault.db`.

---

## 5. REVISION HISTORY & GOVERNANCE
* **v1.0.0:** Established local LoRaWAN topology, Topp Equation VWC algorithms, and zero-cloud MQTT ingestion rules.
* **Approved By:** Jeffery Humphrey, Founder & CEO
* **Enforcement:** Sovereign Master Console Runtime Protocol
