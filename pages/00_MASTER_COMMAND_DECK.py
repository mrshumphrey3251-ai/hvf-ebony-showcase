import streamlit as st
import time

st.set_page_config(page_title="EBONY // OMNI-MATRIX", layout="wide", initial_sidebar_state="expanded")

# --- MODULAR SCADA ROUTER (SESSION STATE) ---
if "scada_view" not in st.session_state:
    st.session_state.scada_view = "MACRO"

def route_view(view):
    st.session_state.scada_view = view

st.markdown("# 🦅 MASTER COMMAND DECK // SCADA ROUTER")
st.caption("TIER-1 EXECUTIVE OVERRIDE // OMNI-MATRIX COLLECTIVE AND INDIVIDUAL CONTROL")
st.divider()

# --- DYNAMIC VERTICAL REGISTRY ---
verticals = {
    "🌾 AGRICULTURE": ["ACTUATE PIVOTS", "FERTIGATION OVERRIDE", "HALT HARVESTERS"],
    "🚛 LOGISTICS": ["REROUTE SWARM", "LOCK DOWN FLEET", "EMERGENCY CHARGE"],
    "🚁 DEFENSE": ["PERIMETER SWEEP", "WEAPONS HOT", "SCRAMBLE INTERCEPTORS"],
    "⚡ ENERGY": ["DUMP TO MARKET", "ISLAND GRID", "SCRAM REACTORS"],
    "🏭 MANUFACTURING": ["OVERDRIVE SPINDLES", "EMERGENCY QUENCH", "HALT ASSEMBLY"],
    "📡 COMMS": ["ROTATE TOPOLOGY", "VHF FALLBACK", "BURN ENCRYPTION"],
    "🏦 FINANCE": ["FIRE PROCUREMENT", "FREEZE TREASURY", "LIQUIDATE TO COLD STORAGE"],
    "🏥 HEALTHCARE": ["DISPATCH MED-EVAC", "BIO-LOCKDOWN", "PURGE HVAC"],
    "🛰️ AEROSPACE": ["PULSE PHASED ARRAY", "LAUNCH INTERCEPTOR", "JAMMING OVERRIDE"],
    "🏗️ CIVIL ENG": ["HALT EXTRUSION", "ACTUATE DAMPERS", "LOCK BLAST DOORS"],
    "⛏️ MINING": ["THROTTLE TBM", "ABORT SUBTERRANEAN", "VENTILATION OVERDRIVE"],
    "🌊 DEEP OCEAN": ["FEATHER TURBINES", "FIRE ACOUSTIC SHOCK", "SEAL VAULTS"],
    "🔐 CRYPTO CYBER": ["DEPLOY HONEYPOTS", "ZERO-DAY WIPE", "LOCKOUT ENCLAVES"],
    "💧 HYDROLOGY": ["OVERDRIVE AWG", "SEAL AQUIFER", "FLUSH RESERVOIR"],
    "📦 WAREHOUSING": ["PRE-KIT PAYLOADS", "HYPOXIC VENT", "LOCK KINEMATICS"]
}

# --- VIEW 1: MACRO (COLLECTIVE MONITORING) ---
if st.session_state.scada_view == "MACRO":
    st.subheader("MACRO VIEW // COLLECTIVE MONITORING")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("OpEx Burn Rate", "$142.50/hr", "-1.2%")
    m2.metric("Sovereign Power", "12.4 MW", "Surplus")
    m3.metric("Hydro Reserves", "4.2M Gal", "Optimal")
    m4.metric("Swarm Cohesion", "100%", "Secure")
    st.divider()
    
    cols = st.columns(5)
    for idx, (v_name, actions) in enumerate(verticals.items()):
        with cols[idx % 5]:
            st.markdown(f"**{v_name}**")
            st.markdown("STATUS: `ONLINE`")
            st.button(f"ACCESS COMMAND CENTER", key=f"btn_{v_name}", on_click=route_view, args=(v_name,), use_container_width=True)
            st.write("---")

# --- VIEW 2: MICRO (INDIVIDUAL MONITORING) ---
else:
    v_name = st.session_state.scada_view
    st.button("◄ RETURN TO MACRO GRID", on_click=route_view, args=("MACRO",))
    st.divider()
    
    st.header(f"MICRO VIEW // {v_name} COMMAND CENTER")
    
    # Localized SCADA Telemetry
    c1, c2, c3 = st.columns(3)
    c1.metric("Sub-System Status", "NOMINAL", "0 Errors")
    c2.metric("Node Latency", "4ms", "Optimal")
    c3.metric("Power Draw", "840 kW", "Stable")
    
    st.divider()
    st.subheader("LOCALIZED KINETIC OVERRIDES")
    
    actions = verticals[v_name]
    a_cols = st.columns(len(actions))
    for idx, action in enumerate(actions):
        with a_cols[idx]:
            if st.button(action, use_container_width=True, type="primary"):
                with st.spinner('Executing cryptographic handshake...'):
                    time.sleep(0.5)
                st.error(f"**EXECUTED:** {action} protocol initiated across {v_name}.")
