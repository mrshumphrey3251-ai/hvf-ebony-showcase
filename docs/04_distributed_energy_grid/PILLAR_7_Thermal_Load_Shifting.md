# 🧊 PILLAR 7: THERMAL LOAD SHIFTING
**DOCUMENT TYPE:** COMPREHENSIVE TRAINING MANUAL & TIER-1 SCHEMATIC
**INSTRUCTOR & SYSTEM:** EBONY (MASTER EDGE NODE)
**FORMAT:** SITUATION REPORT (SITREP)

---
## 1. MISSION STATEMENT
**Objective:** Store massive amounts of cooling capacity as physical ice during the night, deploying it during peak daytime heat to mathematically eliminate HVAC energy spikes.

**Key Performance Indicators (KPIs):**

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Phase Change** | 100% water to ice by 0500 hrs | Tank thermal sensors |
| **Peak Load Reduction** | > 40% drop in daytime kW draw | Facility smart meters |

---
## 2. ZERO-TO-CEO OVERVIEW
Running air conditioning during a 100°F day requires massive electricity. We do not do it. At 2:00 AM, when ambient temperatures are low and grid power is virtually free, Ebony runs industrial chillers to freeze thousands of gallons of water in insulated subterranean tanks. During the day, the chillers turn off, and facility air is blown over the ice.

---
## 3. TIER-1 TECHNICAL SCHEMATIC
### 3.1 System Architecture Diagram

```text
+-------------------+          +-------------------+          +-------------------+
| Off-Peak Grid     |  Temp    |   Edge Node (EB)  |  Freeze  | Subterranean      |
| (Cheap Power)     |=======>  | (Thermo-Calculus) |=======>  | Ice Bank Tanks    |
+-------------------+  Data    +-------------------+  Cmd     +-------------------+
```

### 3.2 Latent Heat Calculus
Ebony calculates the total stored cooling capacity ($Q_{latent}$) using the mass of the water ($m$) and the latent heat of fusion ($L_f$):

```text
Q_{latent} = m \cdot L_f
```

### 3.3 Bare-Metal Execution Code (Node.js Reference)

```javascript
function calculateThermalShift(hourOfDay, gridPrice, iceTankPercentage) {
    // WATCHDOG: Only freeze when economically viable or solar is overflowing
    if (hourOfDay >= 2 && hourOfDay <= 5 && gridPrice < 0.05 && iceTankPercentage < 100) {
        engageIndustrialChillers();
    } else if (hourOfDay >= 12 && hourOfDay <= 17) {
        // Peak heat: Shut down chillers, route air over ice banks
        shutdownChillers();
        actuateIceBlowerFans();
    }
}

function engageIndustrialChillers() {}
function shutdownChillers() {}
function actuateIceBlowerFans() {}
```

---
## 4. EXECUTIVE INTERACTION & MANUAL OVERRIDE (SOP)

| Step | Action | System Response | Safety Note |
| :--- | :--- | :--- | :--- |
| 1 | Operator logs into Energy Dashboard. | Authenticates via SSO. | -- |
| 2 | Navigate to ⚡ Energy → Thermal Load Shifting. | Live ice-tank phase percentage renders. | Monitor off-peak pricing. |
| 3 | Adjust grid price to peak levels in sandbox. | Node kills chillers and shifts to ice-blowers. | Confirms load shift. |
| 4 | Click 🔴 LIVE EXECUTION → HALT. | Kills all HVAC blowers and chillers. | Facility temp will rise rapidly. |

---
## 5. OPERATIONAL CHECKLIST
### 5.1 Pre-Mission (Thermal Audit)
*   [ ] **Coolant Integrity:** Confirm industrial chiller glycol levels are nominal.
*   [ ] **Tank Insulation:** Verify subterranean thermal leakage is < 1% per 24hrs.
*   [ ] **Blower Fans:** Test air-handler RPM and CFM output.