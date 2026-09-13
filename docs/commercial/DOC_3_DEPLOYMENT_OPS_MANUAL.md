# 🚀 DOC 3: HVF DEPLOYMENT GUIDE & OPS MANUAL
**Document ID:** HVF-COM-DOC-003  
**Classification:** Commercial Operations / Field Deployment  
**Author:** Jeffery Humphrey, Founder & CEO, Humphrey Virtual Farms  
**Target Systems:** Field Engineers, Enterprise Integration Teams  

---

## 1. PRE-DEPLOYMENT SITE READINESS

### 1.1 Physical & Network Prerequisites
Before the HVF Edge Node arrives on-site, the environment must be hardened to strict enterprise standards:
* **Power Redundancy:** The Master Edge Node and primary LoRaWAN gateways must be connected to an Uninterruptible Power Supply (UPS) capable of sustaining operations for a minimum of 4 hours during rural grid failure.
* **Network Segregation:** A dedicated, air-gapped `[REDACTED_ISOLATED_SUBNET]` internal subnet must be established. Kinetic hardware must not share a VLAN with administrative or public-facing internet traffic.

---

## 2. MASTER EDGE NODE BOOTSTRAPPING

### 2.1 Core System Initialization
1. **Power On:** Connect the pre-configured HVF Master Node to the segregated network and boot the system.
2. **Daemon Verification:** Open the local terminal and verify the core service daemons are running:
   * `systemctl status ollama` (Neural Engine)
   * `systemctl status mediamtx` (Drone Vision Subsystem)
3. **Database Check:** Confirm the instantiation of `[REDACTED_VAULT_DB]` in the root operating directory.

---

## 3. KINETIC & IOT HARDWARE BINDING

### 3.1 Provisioning the Field Assets
Every physical asset must be cryptographically bound to the Edge Node to authorize actuation commands.
1. **LoRaWAN Soil Probes:** Input the DevEUI and AppKey into the console's **⚙️ Empire Config** module. Verify telemetry packets are intercepting locally via the MQTT broker.
2. **UAV Hangars & Irrigation Valves:** Assign static IPs to the hardware and register their MAC addresses within the `[REDACTED_SECTOR_VAULT]`. The Ebony engine will immediately establish a heartbeat ping to verify interlock readiness.

---

## 4. EXECUTIVE HANDOVER & CRYPTOGRAPHIC SECUREMENT

### 4.1 Master Identity Establishment
HVF operates on a Zero-Trust local identity model. The final step of deployment transfers absolute ownership to the site CEO.
1. The integration engineer generates a new asymmetric key pair and a symmetric `[CLASSIFIED_ENCRYPTION]` `.env` key on the Edge Node.
2. The site CEO inputs their personal password, which the system immediately hashes using PBKDF2 and commits to the vault.
3. The default Executive Kinetic PIN is overwritten and set by the CEO (replacing the factory `[REDACTED_EXECUTIVE_PIN]` default).
4. The integration engineer’s access is formally downgraded to TIER 2 (Super Admin) or completely revoked, establishing the site CEO as the sole Tier 1 Master Founder.
