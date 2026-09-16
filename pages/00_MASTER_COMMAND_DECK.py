import streamlit as st
import time

st.set_page_config(page_title="EBONY // OMNI-MATRIX", layout="wide", initial_sidebar_state="expanded")

st.markdown("# 🦅 MASTER COMMAND DECK")
st.caption("TIER-1 EXECUTIVE OVERRIDE // SOVEREIGN OMNI-MATRIX")
st.divider()

# --- 1. GLOBAL TELEMETRY MATRIX ---
st.subheader("GLOBAL TELEMETRY")
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("OpEx Burn Rate", "$142.50/hr", "-1.2% (Optimized)")
m2.metric("Sovereign Power", "12.4 MW", "Surplus (Arbitrage)")
m3.metric("Hydro Reserves", "4.2M Gal", "+12k Gal (Condensation)")
m4.metric("Swarm Cohesion", "100%", "0 Nodes Offline")
m5.metric("Crypto Treasury", "$4.2M", "+$150k (Yield)")

st.divider()

# --- 2. 15-VERTICAL KINETIC OVERRIDE VECTORS ---
st.subheader("OMNI-MATRIX KINETIC OVERRIDES")

verticals = {
    "🌾 AGRICULTURE": [{"label": "ACTUATE PIVOTS", "type": "secondary", "msg": "Center pivots marching to target coordinates."}, {"label": "FERTIGATION", "type": "primary", "msg": "NPK routing active."}],
    "🚛 LOGISTICS": [{"label": "ROUTING OVERRIDE", "type": "secondary", "msg": "AGV swarm recalculating paths."}, {"label": "LOCK DOWN FLEET", "type": "primary", "msg": "All vehicles immobilized."}],
    "🚁 DEFENSE": [{"label": "PERIMETER SWEEP", "type": "secondary", "msg": "Patrol drones deployed."}, {"label": "WEAPONS HOT", "type": "primary", "msg": "Lethal countermeasures authorized."}],
    "⚡ ENERGY": [{"label": "DUMP TO MARKET", "type": "secondary", "msg": "Arbitrage settlement active."}, {"label": "ISLAND GRID", "type": "primary", "msg": "Civilian grid severed."}],
    "🏭 MANUFACTURING": [{"label": "SPINDLE OVERDRIVE", "type": "secondary", "msg": "CNC production increased."}, {"label": "EMERGENCY QUENCH", "type": "primary", "msg": "Reflow ovens flooded with nitrogen."}],
    "📡 COMMS": [{"label": "ROTATE TOPOLOGY", "type": "secondary", "msg": "Subnet IP hopping initiated."}, {"label": "VHF FALLBACK", "type": "primary", "msg": "Fiber severed. Analog comms active."}],
    "🏦 FINANCE": [{"label": "PROCUREMENT", "type": "secondary", "msg": "Smart contracts fired."}, {"label": "FREEZE TREASURY", "type": "primary", "msg": "Assets shifted to cold storage."}],
    "🏥 HEALTHCARE": [{"label": "MED-EVAC", "type": "secondary", "msg": "Trauma drone dispatched."}, {"label": "BIO-LOCKDOWN", "type": "primary", "msg": "Sectors sealed. UV-C active."}],
    "🛰️ AEROSPACE": [{"label": "SCRAMBLE RADAR", "type": "secondary", "msg": "Phased array sweeping."}, {"label": "INTERDICT", "type": "primary", "msg": "Hunter-Killer swarm deployed."}],
    "🏗️ CIVIL ENG": [{"label": "HALT EXTRUSION", "type": "secondary", "msg": "3D printing paused."}, {"label": "ACTUATE DAMPERS", "type": "primary", "msg": "Seismic base isolation locked."}],
    "⛏️ MINING": [{"label": "BORE ADVANCE", "type": "secondary", "msg": "TBM thrust increased."}, {"label": "ABORT SECTOR", "type": "primary", "msg": "Mine evacuation initiated."}],
    "🌊 DEEP OCEAN": [{"label": "TURBINE FEATHER", "type": "secondary", "msg": "Tidal blades neutralized."}, {"label": "ACOUSTIC SHOCK", "type": "primary", "msg": "Subaquatic deterrence fired."}],
    "🔐 CRYPTO CYBER": [{"label": "DEPLOY HONEYPOTS", "type": "secondary", "msg": "Phantom servers online."}, {"label": "ZERO-DAY WIPE", "type": "primary", "msg": "Cryptographic keys incinerated."}],
    "💧 HYDROLOGY": [{"label": "AWG OVERDRIVE", "type": "secondary", "msg": "Condensation turbines at max."}, {"label": "SEAL AQUIFER", "type": "primary", "msg": "Subterranean valves locked."}],
    "📦 WAREHOUSING": [{"label": "KITTING PROTOCOL", "type": "secondary", "msg": "ASRS pre-assembling payloads."}, {"label": "HYPOXIC VENT", "type": "primary", "msg": "Nitrogen flooded. Fire impossible."}]
}

# Dynamically generate the 3x5 command grid
vert_items = list(verticals.items())
cols_per_row = 5

for i in range(0, len(vert_items), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        if i + j < len(vert_items):
            vert_name, controls = vert_items[i + j]
            with col:
                st.markdown(f"**{vert_name}**")
                for ctrl in controls:
                    if st.button(ctrl["label"], key=f"{vert_name}_{ctrl['label']}", use_container_width=True, type=ctrl["type"]):
                        with st.spinner('Cryptographic handshake...'):
                            time.sleep(0.4) 
                        if ctrl["type"] == "primary":
                            st.error(f"**EXECUTED:** {ctrl['msg']}")
                        else:
                            st.success(f"**EXECUTED:** {ctrl['msg']}")
    st.write("") 
