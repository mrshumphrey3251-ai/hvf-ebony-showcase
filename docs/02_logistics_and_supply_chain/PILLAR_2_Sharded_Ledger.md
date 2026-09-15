# 📦 PILLAR 2: SHARDED TSDB LEDGER
**DOCUMENT TYPE:** COMPREHENSIVE TRAINING MANUAL & TIER-1 SCHEMATIC
**INSTRUCTOR & SYSTEM:** EBONY (MASTER EDGE NODE)
**FORMAT:** SITUATION REPORT (SITREP)

---
## 1. MISSION STATEMENT
**Objective:** Maintain a decentralized, highly-available Time-Series Database (TSDB) capable of recording millions of logistics events with zero indexing lag, immune to public internet outages.

**Key Performance Indicators (KPIs):**

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Write Velocity** | > 100,000 writes per second | Local NVMe benchmark telemetry |
| **Indexing Latency** | < 5ms per transaction | Microsecond timestamp deltas |
| **Failover Time** | < 50ms to emergency memory buffer | IOPS load monitoring |
| **Ledger Uptime** | 99.999% (Air-Gapped) | Local hardware watchdog |

---
## 2. ZERO-TO-CEO OVERVIEW
*   **Normal Operation:** Logistics events (cargo weight, gate access) are written instantly to localized PCIe 4.0 NVMe RAID arrays.
*   **Threat Scenario:** Network ingestion spikes or a physical drive fails, threatening data loss.
*   **Resilience Layer:** Ebony autonomously "shards" the database, distributing the ledger across multiple high-speed drives simultaneously. Overflow is dynamically routed to emergency memory buffers.
*   **Result:** The system never stops writing. Every action is mathematically preserved.

---
## 3. TIER-1 TECHNICAL SCHEMATIC
### 3.1 System Architecture Diagram

```text
+-------------------+          +-------------------+          +-------------------+
| Telemetry Ingest  |  Data    |   Edge Node (EB)  |  Shard   | NVMe RAID 10 Array|
| (UWB / MQTT)      |=======>  |  (Ledger Engine)  |=======>  | (Distributed DB)  |
+-------------------+          +-------------------+          +-------------------+
                                       | TPM 2.0 |
                                       +---------+
                                       (Signature)
```

*   **Storage Medium:** Localized PCIe 4.0 NVMe SSDs in RAID 10 configuration ($N_{shards} = 8$).
*   **Security Protocol:** On-device Hyperledger Fabric. All entries signed by the Edge Node's physical TPM 2.0 chip.

### 3.2 Cryptographic Sharding Calculus
Ebony determines the exact physical NVMe drive ($S_{index}$) for every telemetry packet using a deterministic cryptographic sharding algorithm:

```text
S_{index} = \text{SHA-256}(Asset_{ID} + T_{nano}) \pmod{N_{shards}}
```

### 3.3 Bare-Metal Execution Code (Go Reference)

```go
package ledger

import (
    "fmt"
    "time"
)

type CargoEvent struct {
    AssetID      string
    Weight       float64
    Timestamp    int64
    TPMSignature string
}

func AppendToLedger(event CargoEvent, shard map[string][]CargoEvent, diskLoad float64) {
    // WATCHDOG: If disk I/O exceeds 80%, flush to secondary memory buffers
    if diskLoad > 0.80 {
        execute_emergency_memory_flush(event)
        return
    }

    event.Timestamp = time.Now().UnixNano()
    shard[event.AssetID] = append(shard[event.AssetID], event)
}

func execute_emergency_memory_flush(e CargoEvent) {}
```

---
## 4. EXECUTIVE INTERACTION & MANUAL OVERRIDE (SOP)

| Step | Action | System Response | Safety Note |
| :--- | :--- | :--- | :--- |
| 1 | Operator logs into the Logistics Dashboard. | Authenticates via SSO; TPM session token generated. | Validate local network isolation. |
| 2 | Navigate to 🚛 Logistics → Sharded Ledger. | Live IOPS and Write Velocity metrics stream. | Confirm RAID array health. |
| 3 | Simulate write-load spike via sandbox dial. | System triggers sharding protocol to distribute load. | Observe failover latency. |
| 4 | Click 🔴 LIVE EXECUTION → HALT. | Ledger freezes. RAM buffers cache incoming packets. | Ensure halt < 60s to prevent RAM overflow. |

---
## 5. OPERATIONAL CHECKLIST
### 5.1 Pre-Mission (Daily Audit)
*   [ ] **RAID Integrity:** Verify NVMe array SMART status shows 100% health.
*   [ ] **TPM Attestation:** Confirm ledger signing keys are actively rotating.
*   [ ] **RAM Buffer:** Ensure secondary emergency cache is cleared and ready.