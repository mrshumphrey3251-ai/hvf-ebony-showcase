# 🌋 PILLAR 2: GEOTHERMAL BASE-LOAD
**DOCUMENT TYPE:** COMPREHENSIVE TRAINING MANUAL & TIER-1 SCHEMATIC
**INSTRUCTOR & SYSTEM:** EBONY (MASTER EDGE NODE)
**FORMAT:** SITUATION REPORT (SITREP)

---
## 1. MISSION STATEMENT
**Objective:** Maintain 100% of the facility's baseline Megawatt power requirement using mathematically stabilized subterranean heat, immune to weather fluctuations.

**Key Performance Indicators (KPIs):**

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Thermal Output** | Constant 5.0 MW baseline | Turbine RPM / Alternator output |
| **Flow Rate** | > 200 L/s subterranean brine | Magnetic flow meters |
| **Injection Temp** | < 70°C return fluid | PT100 RTD thermal sensors |
| **System Uptime** | 99.9% 24/7/365 | TSDB generation ledger |

---
## 2. ZERO-TO-CEO OVERVIEW
*   **Normal Operation:** Civilian solar farms die at night, and wind farms die when the air is still.
*   **Threat Scenario:** A prolonged winter storm blacks out the sun and freezes wind turbines, threatening the farm's survival.
*   **Resilience Layer:** We tap directly into the earth's crust. Ebony manages high-pressure brine wells, routing subterranean heat through binary-cycle turbines to generate electricity 24 hours a day, completely ignoring surface weather.
*   **Result:** Absolute, uninterruptible sovereign base-load power.

---
## 3. TIER-1 TECHNICAL SCHEMATIC
### 3.1 System Architecture Diagram

```text
+-------------------+          +-------------------+          +-------------------+
| Production Well   |  Heat    |   Edge Node (EB)  |  Steam   | Binary Cycle      |
| (Geothermal Brine)|=======>  | (Thermo-Calculus) |=======>  | Turbine Generator |
+-------------------+  Exch.   +-------------------+  Cmd     +-------------------+
```

### 3.2 Thermodynamic Enthalpy Calculus
Ebony calculates the mass flow rate ($\dot{m}$) required to maintain exact turbine wattage based on subterranean fluid enthalpy ($h$):

```text
W_{turbine} = \dot{m} \cdot \eta_{iso} \cdot (h_{in} - h_{out})
```

### 3.3 Bare-Metal Execution Code (Python Reference)

```python
def regulate_geothermal_flow(target_mw: float, enthalpy_in: float, enthalpy_out: float) -> float:
    efficiency = 0.85 # Isentropic turbine efficiency
    
    # WATCHDOG: Prevent turbine over-spin by capping mass flow
    required_flow = (target_mw * 1000) / (efficiency * (enthalpy_in - enthalpy_out))
    
    if required_flow > 250.0:
        return 250.0 # Hardware structural limit (L/s)
        
    return required_flow
```

---
## 4. EXECUTIVE INTERACTION (SOP)
Navigate to **⚡ Energy → Geothermal Base-Load**. Adjust the brine injection temperatures to watch the Edge Node dynamically calculate fluid flow to stabilize the 5.0 MW baseline.