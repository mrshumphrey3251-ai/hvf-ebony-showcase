import streamlit as st
import time

st.set_page_config(page_title="EBONY // OMNI-MATRIX", layout="wide", initial_sidebar_state="expanded")

# --- MODULAR SCADA ROUTER (SESSION STATE) ---
if "scada_view" not in st.session_state:
    st.session_state.scada_view = "MACRO"

def route_view(view):
    st.session_state.scada_view = view

st.markdown("# 🦅 MASTER COMMAND DECK // SCADA ROUTER")
st.caption("TIER-1 EXECUTIVE OVERRIDE // OMNI-MATRIX COLLECTIVE AND GRANULAR CONTROL")
st.divider()

# --- DYNAMIC VERTICAL REGISTRY ---
verticals = {
    "🌾 AGRICULTURE": ["EMERGENCY HALT PIVOTS", "PURGE FERTIGATION", "SCRAM TRACTORS"],
    "🚛 LOGISTICS": ["LOCK DOWN FLEET", "REROUTE TO CHARGE", "ABORT MANIFEST"],
    "🚁 DEFENSE": ["WEAPONS HOT", "SCRAMBLE INTERCEPTORS", "RECALL SWARM"],
    "⚡ ENERGY": ["ISLAND GRID", "SCRAM REACTORS", "DUMP TO MARKET"],
    "🏭 MANUFACTURING": ["EMERGENCY QUENCH", "HALT ASSEMBLY", "VENT OZONE"],
    "📡 COMMS": ["BURN ENCRYPTION", "VHF FALLBACK", "ROTATE TOPOLOGY"],
    "🏦 FINANCE": ["FREEZE TREASURY", "LIQUIDATE TO COLD", "FIRE PROCUREMENT"],
    "🏥 HEALTHCARE": ["BIO-LOCKDOWN", "PURGE HVAC", "DISPATCH MED-EVAC"],
    "🛰️ AEROSPACE": ["LAUNCH INTERCEPTOR", "JAMMING OVERRIDE", "PULSE PHASED ARRAY"],
    "🏗️ CIVIL ENG": ["ACTUATE DAMPERS", "LOCK BLAST DOORS", "HALT EXTRUSION"],
    "⛏️ MINING": ["ABORT SUBTERRANEAN", "VENTILATION OVERDRIVE", "THROTTLE TBM"],
    "🌊 DEEP OCEAN": ["FIRE ACOUSTIC SHOCK", "SEAL VAULTS", "FEATHER TURBINES"],
    "🔐 CRYPTO CYBER": ["ZERO-DAY WIPE", "LOCKOUT ENCLAVES", "DEPLOY HONEYPOTS"],
    "💧 HYDROLOGY": ["SEAL AQUIFER", "FLUSH RESERVOIR", "OVERDRIVE AWG"],
    "📦 WAREHOUSING": ["HYPOXIC VENT", "LOCK KINEMATICS", "PRE-KIT PAYLOADS"]
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

# --- VIEW 2: MICRO (GRANULAR ASSET CONTROL) ---
else:
    v_name = st.session_state.scada_view
    st.button("◄ RETURN TO MACRO GRID", on_click=route_view, args=("MACRO",))
    st.divider()
    
    st.header(f"MICRO VIEW // {v_name} COMMAND CENTER")
    
    # Localized SCADA Telemetry
    c1, c2, c3 = st.columns(3)
    c1.metric("Sector Status", "NOMINAL", "0 Errors")
    c2.metric("Active Nodes", "142", "+2")
    c3.metric("Power Draw", "840 kW", "Stable")
    
    st.divider()
    
    # --- GRANULAR CONTROL MATRIX ---
    st.subheader("GRANULAR ASSET CONTROL")
    st.caption("Target individual hardware nodes. Unselected nodes will remain in their current operational state.")
    
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    
    with col1:
        st.markdown("**1. TARGET DESIGNATION**")
        target_node = st.selectbox("Isolate Specific Hardware:", 
                                   ["Node-Alpha-01", "Node-Bravo-02", "Node-Charlie-03", "Node-Delta-04", "TARGET ALL NODES"])
        st.write(f"**Target Lock:** `{target_node}`")
        
    with col2:
        st.markdown("**2. STATE TOGGLES**")
        state_pwr = st.toggle("Main Power Relay", value=True)
        state_vlv = st.toggle("Primary Valve/Drive", value=False)
        state_aux = st.toggle("Auxiliary Sub-System", value=True)
        
    with col3:
        st.markdown("**3. KINETIC PARAMETERS**")
        thrust_rpm = st.slider("Actuation Rate / Flow (%)", 0, 100, 35)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("EXECUTE SURGICAL COMMAND", type="primary", use_container_width=True):
            with st.spinner("Executing targeted handshake..."):
                time.sleep(0.6)
            st.success(f"**LOCKED:** `{target_node}` adjusted. PWR:{state_pwr} | VLV:{state_vlv} | RATE: {thrust_rpm}%")

    st.divider()
    
    # --- GLOBAL EMERGENCY OVERRIDES ---
    st.subheader("GLOBAL SECTOR OVERRIDES (EMERGENCY ONLY)")
    st.caption("Warning: These commands affect all nodes simultaneously across the vertical.")
    actions = verticals[v_name]
    a_cols = st.columns(len(actions))
    for idx, action in enumerate(actions):
        with a_cols[idx]:
            if st.button(action, use_container_width=True):
                with st.spinner('Executing global override...'):
                    time.sleep(0.5)
                st.error(f"**EXECUTED:** {action} protocol forced across {v_name}.")
