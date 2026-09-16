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

st.subheader("MICRO VIEW // KINETIC VERTICALS")
tab1, tab2, tab3 = st.tabs(["🌾 AGRICULTURE", "🏗️ WAREHOUSING", "⚡ ENERGY GRID"])

with tab1:
    st.write("### 🌾 VERTICAL 04: PRECISION AGRICULTURE")
    st.write("Autonomous Irrigation, Soil Telemetry, and Drone Deployment.")
    if st.button("ACTUATE IRRIGATION GRID", key="ag_1"):
        st.success("KINETIC COMMAND SENT: Irrigation Grid Online.")

with tab2:
    st.write("### 🏗️ VERTICAL 15: WAREHOUSING")
    st.write("ASRS Gantries, Inventory Routing, and Hypoxic Bio-Vaults.")
    if st.button("TRIGGER ASRS GANTRIES", key="wh_1"):
        st.success("KINETIC COMMAND SENT: ASRS Routing Active.")

with tab3:
    st.write("### ⚡ VERTICAL 01: ENERGY GRID")
    st.write("Micro-Grid Switching, Load Balancing, and Battery Reserves.")
    if st.button("INITIALIZE BATTERY BACKUP", key="eg_1"):
        st.success("KINETIC COMMAND SENT: Battery Reserves Online.")
