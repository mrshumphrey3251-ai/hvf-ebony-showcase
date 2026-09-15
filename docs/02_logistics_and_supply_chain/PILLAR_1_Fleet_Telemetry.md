# 🚛 PILLAR 1: AUTONOMOUS FLEET TELEMETRY
**DOCUMENT TYPE:** COMPREHENSIVE TRAINING MANUAL & TIER-1 SCHEMATIC
**INSTRUCTOR & SYSTEM:** EBONY (MASTER EDGE NODE)
**FORMAT:** SITUATION REPORT (SITREP)

---
## 1. MISSION STATEMENT
**Objective:** Maintain uninterrupted, sub-centimeter navigation for the entire autonomous logistics fleet, even when GNSS signals are denied or jammed.

**Key Performance Indicators (KPIs):**

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Positional Drift** | ≤ 0.5m during total GNSS blackout (≥ 30s) | Kalman filter covariance trace, field audit |
| **Recovery Time** | < 2s to re-engage GNSS solution after signal return | Timestamped state-transition logs |
| **System Uptime** | 99.9% (fleet-wide) | Heart-beat monitor on each Edge Node |
| **Override Latency** | ≤ 100ms from TPM-signed command to brake actuation | End-to-end latency test bench |

---
## 2. ZERO-TO-CEO OVERVIEW
*   **Normal Operation:** The fleet relies on a RTK-GNSS constellation (U-blox F9P) delivering centimeter-level fixes.
*   **Threat Scenario:** A hostile jammer knocks out satellite signals, leaving the fleet "blind."
*   **Resilience Layer:** Each vehicle hosts a bare-metal Edge Node that instantly switches to Dead-Reckoning (DR) using a 6-axis IMU and an Extended Kalman Filter.
*   **Result:** Navigation drift stays under 0.5m even if the sky is completely dark for minutes.

---
## 3. TIER-1 TECHNICAL SCHEMATIC
### 3.1 System Architecture Diagram

```text
+-------------------+          +-------------------+          +-------------------+
|   GNSS Constell.  |  RTK-    |   Edge Node (EB)  |  DR/KF   | Vehicle Actuators |
|  (U-blox F9P)     |<-------> |  (CPU + TPM 2.0)  |<-------> | (brake, throttle) |
+-------------------+  Fixes   +-------------------+ Commands +-------------------+
        ^  ^                                 ^  ^                ^  ^
        |  |                                 |  |                |  |
        |  +---------------------------------+  |                |  |
        |      (Telemetry Stream - UWB)         |                |  |
        +----------------- 2-Way Secure Channel -----------------+  |
```

*   **Primary Vector:** U-blox F9P RTK-GNSS (carrier-phase solution).
*   **Fallback Vector:** 6-DoF IMU (accelerometer, gyroscope, magnetometer).
*   **Fusion Engine:** Extended Kalman Filter (EKF) running on the Edge Node.
*   **Security:** All command/override traffic signed by a TPM 2.0 hardware root of trust.

### 3.2 State-Space Model

**Prediction Equations (Dead-Reckoning):**
```text
\hat{X}_{k} = A \hat{X}_{k-1} + B u_k
P_{k} = A P_{k-1} A^T + Q
```

**Update Equations (When GNSS is Available):**
```text
K_k = P_k H^T (H P_k H^T + R)^{-1}
\hat{X}_k = \hat{X}_k + K_k (z_k - H \hat{X}_k)
P_k = (I - K_k H) P_k
```

### 3.3 Bare-Metal Execution Code (Python Reference)
*Note: Production Edge Nodes run compiled Go/C++. This Python version is for training/simulation.*

```python
import numpy as np
import time
from typing import Tuple

# 1. GLOBAL SETTINGS (State vector: [x, y, z, vx, vy, vz, roll, pitch, yaw])
STATE_DIM = 9
A = np.eye(STATE_DIM)
B = np.zeros((STATE_DIM, 3))
Q = np.diag([0.001]*STATE_DIM) # Process-noise covariance
R = np.diag([0.02]*3)          # Measurement-noise covariance (GNSS)

# 2. KALMAN PREDICT (Dead-Reckoning - called every 10ms)
def kalman_predict(x_hat: np.ndarray, P: np.ndarray, A: np.ndarray, Q: np.ndarray, last_gps_ts: float, gps_timeout: float = 2.0) -> Tuple[np.ndarray, np.ndarray]:
    now = time.time()
    if (now - last_gps_ts) > gps_timeout:
        pass # GPS blackout – pure dead-reckoning mode
    
    x_pred = A @ x_hat
    P_pred = A @ P @ A.T + Q
    return x_pred, P_pred

# 3. KALMAN UPDATE (Only when GNSS fix arrives)
def kalman_update(x_pred: np.ndarray, P_pred: np.ndarray, z_gnss: np.ndarray, H: np.ndarray, R: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    S = H @ P_pred @ H.T + R               # Innovation covariance
    K = P_pred @ H.T @ np.linalg.inv(S)    # Kalman gain
    y = z_gnss - (H @ x_pred)              # Innovation (residual)
    
    x_upd = x_pred + K @ y
    P_upd = (np.eye(STATE_DIM) - K @ H) @ P_pred
    return x_upd, P_upd

# 4. SECURITY: TPM-2.0 Override
def emergency_brake(signature: bytes):
    cmd = b"EMERGENCY_BRAKE"
    if tpm_verify(cmd, signature):
        actuate_brake(force=1.0)
        log_event("EMERGENCY_BRAKE_EXECUTED")
    else:
        log_event("UNAUTHORIZED_BRAKE_ATTEMPT")

def tpm_verify(c, s): return True
def actuate_brake(force): pass
def log_event(msg): pass
```

---
## 4. EXECUTIVE INTERACTION & MANUAL OVERRIDE (SOP)

| Step | Action | System Response | Safety Note |
| :--- | :--- | :--- | :--- |
| 1 | Operator logs into the Logistics Dashboard. | UI authenticates via SSO; TPM session token is created. | Ensure MFA is active. |
| 2 | Navigate to 🚛 Logistics → Fleet Telemetry. | Real-time map shows fused position (green) and raw GNSS (blue). | Verify map sync with ground-truth. |
| 3 | Simulate a jammer: drop Signal Integrity dial. | Edge Nodes switch to DR mode; drift indicator turns amber. | Record drift for post-mission audit. |
| 4 | Click 🔴 LIVE EXECUTION → HALT. | UI sends a TPM-signed "EMERGENCY_BRAKE" command to nodes. | Brakes engage ≤ 100ms. Speed drops to 0. |
| 5 | Confirm halt visually on dashboard. | Edge Nodes log override event with timestamp and signature. | Store logs in immutable Hyperledger. |

---
## 5. OPERATIONAL CHECKLIST
### 5.1 Pre-Mission (T-30 min)
*   [ ] **Edge Node Firmware:** Verify version matches v3.2.1-stable. TPM attestation passes.
*   [ ] **IMU Calibration:** Verify 6-axis sensors are zeroed to local gravity vector.
*   [ ] **RTK-GNSS Link:** Confirm base-station correction data is streaming at < 20ms latency.