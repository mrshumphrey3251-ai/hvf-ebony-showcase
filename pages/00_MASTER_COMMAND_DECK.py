import streamlit as st
import time

st.set_page_config(page_title="MASTER COMMAND DECK", layout="wide", initial_sidebar_state="expanded")

st.markdown("# 🦅 MASTER COMMAND DECK")
st.caption("TIER-1 EXECUTIVE OVERRIDE // SOVEREIGN OMNI-MATRIX")
st.divider()

# --- 1. GLOBAL TELEMETRY MATRIX ---
st.subheader("GLOBAL TELEMETRY")
m1, m2, m3, m4 = st.columns(4)
m1.metric("OpEx Burn Rate", "$142.50/hr", "-1.2% (Optimized)")
m2.metric("Sovereign Power", "12.4 MW", "Surplus (Arbitrage Active)")
m3.metric("Hydro Reserves", "4.2M Gal", "+12k Gal (Condensation)")
m4.metric("Swarm Cohesion", "100%", "0 Nodes Offline")

st.divider()

# --- 2. MODULAR KINETIC OVERRIDE VECTORS ---
# Engineered for infinite scalability. Add new buttons to this dictionary without rewriting the UI.
st.subheader("KINETIC OVERRIDE VECTORS")

verticals = {
    "🌾 AGRICULTURE": [
        {"label": "ACTUATE PIVOTS", "type": "secondary", "msg": "Center pivots marching to target coordinates."},
        {"label": "INITIATE FERTIGATION", "type": "primary", "msg": "Peristaltic pumps engaged. NPK routing active."}
    ],
    "🚁 AEROSPACE": [
        {"label": "SCRAMBLE RADAR", "type": "secondary", "msg": "Phased array sweeping for hypersonic signatures."},
        {"label": "LAUNCH INTERDICTORS", "type": "primary", "msg": "Hunter-Killer swarm deployed. Weapons hot."}
    ],
    "🏥 HEALTHCARE": [
        {"label": "DISPATCH MED-EVAC", "type": "secondary", "msg": "Trauma drone dispatched to operator coordinates."},
        {"label": "BIOHAZARD LOCKDOWN", "type": "primary", "msg": "Sectors sealed. UV-C sterilization active."}
    ],
    "⚡ ENERGY": [
        {"label": "DUMP TO MARKET", "type": "secondary", "msg": "Arbitrage settlement active. Generating invoice."},
        {"label": "ISLAND GRID", "type": "primary", "msg": "Civilian grid severed. Sovereign power only."}
    ]
}

# Dynamically generate the command grid
columns = st.columns(len(verticals))

for idx, (vert_name, controls) in enumerate(verticals.items()):
    with columns[idx]:
        st.markdown(f"### {vert_name}")
        for ctrl in controls:
            if st.button(ctrl["label"], use_container_width=True, type=ctrl["type"]):
                with st.spinner('Executing cryptographic handshake...'):
                    time.sleep(0.5) # Simulate hardware latency
                if ctrl["type"] == "primary":
                    st.error(f"**COMMAND EXECUTED:** {ctrl['msg']}")
                else:
                    st.success(f"**COMMAND EXECUTED:** {ctrl['msg']}")
