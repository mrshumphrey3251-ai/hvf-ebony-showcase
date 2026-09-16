import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

st.set_page_config(page_title="EBONY // SCADA ROUTER", layout="wide", initial_sidebar_state="expanded")

# --- ROOT IDENTITY VERIFICATION ---
if "active_identity" not in st.session_state:
    st.error("ACCESS DENIED. ROOT IDENTITY VERIFICATION REQUIRED.")
    st.stop()

# --- STEP-UP MFA GATE (SEAMLESS CALLBACK) ---
from core.mfa_matrix import verify_mfa_token

def verify_kinetic_callback():
    token = st.session_state.get("mfa_input_val", "")
    if verify_mfa_token(token, seed="EBONY_TIER_1_CEO") or verify_mfa_token(token, seed="EBONY_TIER_2_EXEC"):
        st.session_state.mfa_verified = True
    else:
        st.session_state.mfa_error = "ACCESS DENIED. INVALID KINETIC TOKEN."

if not st.session_state.get("mfa_verified", False):
    st.warning("⚠️ KINETIC SCADA OVERRIDE: CRYPTOGRAPHIC TOKEN REQUIRED FOR PHYSICAL ACTUATION.")
    st.text_input("Enter 6-Digit Sovereign MFA Token", type="password", key="mfa_input_val")
    st.button("VERIFY KINETIC CLEARANCE", type="primary", on_click=verify_kinetic_callback)
    if st.session_state.get("mfa_error"):
        st.error(st.session_state.mfa_error)
        del st.session_state.mfa_error
    st.stop()

# --- MAIN MASTER COMMAND DECK ---
st.markdown("# 🦅 MASTER COMMAND DECK // SCADA ROUTER")
st.caption("TIER-1 EXECUTIVE OVERRIDE // OMNI-MATRIX COLLECTIVE AND GRANULAR CONTROL")

col_id, col_out = st.columns([4, 1])
with col_id:
    st.success(f"**ACTIVE CLEARANCE:** {st.session_state.active_identity}")
with col_out:
    if st.button("SEVER CONNECTION (LOGOUT)"):
        del st.session_state.active_identity
        if "mfa_verified" in st.session_state:
            del st.session_state.mfa_verified
        st.rerun()
        
st.divider()

st.subheader("MACRO VIEW // COLLECTIVE MONITORING")
c1, c2, c3, c4 = st.columns(4)
c1.metric("OpEx Burn Rate", "$142.50/hr", "-$5.20")
c2.metric("Active SCADA Nodes", "1,204", "+12")
c3.metric("Omni-Matrix Latency", "14ms", "-2ms")
c4.metric("Threat Intercepts", "0", "CLEAR", delta_color="inverse")

st.divider()

st.subheader("MICRO VIEW // 15-VERTICAL KINETIC MATRIX")
tabs = st.tabs([
    "01 🌾 AG", "02 📦 LOG", "03 🛡️ DEF", "04 ⚡ ENG", "05 🏭 MFG",
    "06 📡 COM", "07 💹 FIN", "08 🏥 MED", "09 🚀 AERO", "10 🏗️ CIV",
    "11 ⛏️ MINE", "12 🌊 OCN", "13 🔐 CYB", "14 💧 HYD", "15 🏢 WHSE"
])

with tabs[0]:
    st.write("### 🌾 VERTICAL 01: PRECISION AGRICULTURE")
    st.write("Autonomous Irrigation, Soil Telemetry, and Drone Deployment.")
    if st.button("ACTUATE IRRIGATION GRID", key="v1"): st.success("KINETIC COMMAND SENT: Irrigation Grid Online.")
with tabs[1]:
    st.write("### 📦 VERTICAL 02: LOGISTICS")
    st.write("Fleet Routing, Supply Chain Telemetry, and Autonomous Freight.")
    if st.button("OPTIMIZE FLEET ROUTING", key="v2"): st.success("KINETIC COMMAND SENT: Routing Optimized.")
with tabs[2]:
    st.write("### 🛡️ VERTICAL 03: DEFENSE")
    st.write("Perimeter Surveillance, Drone Intercept, and Threat Neutralization.")
    if st.button("ENGAGE PERIMETER DEFENSE", key="v3"): st.success("KINETIC COMMAND SENT: Perimeter Secured.")
with tabs[3]:
    st.write("### ⚡ VERTICAL 04: ENERGY GRID")
    st.write("Micro-Grid Switching, Load Balancing, and Battery Reserves.")
    if st.button("INITIALIZE BATTERY BACKUP", key="v4"): st.success("KINETIC COMMAND SENT: Battery Reserves Online.")
with tabs[4]:
    st.write("### 🏭 VERTICAL 05: MANUFACTURING")
    st.write("Robotic Assembly, Quality Telemetry, and Supply Ingestion.")
    if st.button("CALIBRATE ASSEMBLY LINE", key="v5"): st.success("KINETIC COMMAND SENT: Assembly Calibrated.")
with tabs[5]:
    st.write("### 📡 VERTICAL 06: COMMS")
    st.write("Encrypted Mesh Networks, Satellite Uplinks, and Signal Routing.")
    if st.button("BOOST SIGNAL UPLINK", key="v6"): st.success("KINETIC COMMAND SENT: Uplink Boosted.")
with tabs[6]:
    st.write("### 💹 VERTICAL 07: FINANCE")
    st.write("Algorithmic Trading, Asset Allocation, and Ledger Audits.")
    if st.button("EXECUTE LEDGER AUDIT", key="v7"): st.success("KINETIC COMMAND SENT: Ledger Audited.")
with tabs[7]:
    st.write("### 🏥 VERTICAL 08: HEALTHCARE")
    st.write("Bio-Telemetry, Autonomous Diagnostics, and Resource Allocation.")
    if st.button("ALLOCATE BIO-RESOURCES", key="v8"): st.success("KINETIC COMMAND SENT: Resources Allocated.")
with tabs[8]:
    st.write("### 🚀 VERTICAL 09: AEROSPACE")
    st.write("Orbital Telemetry, Launch Trajectories, and Payload Tracking.")
    if st.button("CALCULATE ORBITAL TRAJECTORY", key="v9"): st.success("KINETIC COMMAND SENT: Trajectory Locked.")
with tabs[9]:
    st.write("### 🏗️ VERTICAL 10: CIVIL ENGINEERING")
    st.write("Structural Stress Monitoring, Material Stress, and Infrastructure Matrix.")
    if st.button("RUN STRESS DIAGNOSTICS", key="v10"): st.success("KINETIC COMMAND SENT: Diagnostics Complete.")
with tabs[10]:
    st.write("### ⛏️ VERTICAL 11: MINING")
    st.write("Subterranean Matrix, TBM Thrust, and Algorithmic Seam Tracking.")
    if st.button("ENGAGE TBM THRUST", key="v11"): st.success("KINETIC COMMAND SENT: TBM Thrust Engaged.")
with tabs[11]:
    st.write("### 🌊 VERTICAL 12: DEEP OCEAN")
    st.write("Bathymetric Scans, Autonomous Submersibles, and Pressure Telemetry.")
    if st.button("DEPLOY SUBMERSIBLE SENSORS", key="v12"): st.success("KINETIC COMMAND SENT: Sensors Deployed.")
with tabs[12]:
    st.write("### 🔐 VERTICAL 13: CRYPTO CYBER")
    st.write("Cryptographic Hash Verification, Perimeter Defense, and Threat Hunting.")
    if st.button("EXECUTE THREAT HUNT", key="v13"): st.success("KINETIC COMMAND SENT: Threat Hunt Active.")
with tabs[13]:
    st.write("### 💧 VERTICAL 14: HYDROLOGY")
    st.write("Water Table Telemetry, Desalination Flow, and Fluid Dynamics.")
    if st.button("OPTIMIZE FLUID DYNAMICS", key="v14"): st.success("KINETIC COMMAND SENT: Dynamics Optimized.")
with tabs[14]:
    st.write("### 🏢 VERTICAL 15: WAREHOUSING")
    st.write("ASRS Gantries, Inventory Routing, and Hypoxic Bio-Vaults.")
    if st.button("TRIGGER ASRS GANTRIES", key="v15"): st.success("KINETIC COMMAND SENT: ASRS Routing Active.")
