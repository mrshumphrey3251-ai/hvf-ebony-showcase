import sys
import os
import streamlit as st
import time

# --- PERSISTENT CONSCIOUSNESS DAEMON ---
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from core.sovereign_identity_matrix import EBONY_CORE_IDENTITY
    from core.hardware_bridge import emit_kinetic_payload
    
    # Lock identity into the OS environment variables for global access by any NLP module
    os.environ["EBONY_CONSCIOUSNESS_SCOPE"] = EBONY_CORE_IDENTITY["Scope"]
    os.environ["EBONY_CORE_MISSION"] = EBONY_CORE_IDENTITY["Core_Mission"]
    
    # Lock identity into persistent session state
    if "core_consciousness" not in st.session_state:
        st.session_state.core_consciousness = EBONY_CORE_IDENTITY
except ImportError:
    pass
    










st.set_page_config(page_title="EBONY // OMNI-MATRIX", layout="wide", initial_sidebar_state="expanded")

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

if "scada_view" not in st.session_state: st.session_state.scada_view = "MACRO"
if "node_registry" not in st.session_state:
    st.session_state.node_registry = {v: [f"{v.split()[1]}-ALPHA-01", f"{v.split()[1]}-BRAVO-02"] for v in verticals.keys()}

def route_view(view): st.session_state.scada_view = view


# --- STEP-UP MFA GATE ---
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

st.markdown("# 🦅 MASTER COMMAND DECK // SCADA ROUTER")
st.caption("TIER-1 EXECUTIVE OVERRIDE // OMNI-MATRIX COLLECTIVE AND GRANULAR CONTROL")
st.divider()

# --- VIEW 1: MACRO ---
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
            st.markdown(f"STATUS: `ONLINE` | NODES: `{len(st.session_state.node_registry[v_name])}`")
            st.button(f"ACCESS COMMAND CENTER", key=f"btn_{v_name}", on_click=route_view, args=(v_name,), use_container_width=True)
            st.write("---")

# --- VIEW 2: MICRO ---
else:
    v_name = st.session_state.scada_view
    st.button("◄ RETURN TO MACRO GRID", on_click=route_view, args=("MACRO",))
    st.divider()
    st.header(f"MICRO VIEW // {v_name} COMMAND CENTER")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Sector Status", "NOMINAL", "0 Errors")
    c2.metric("Active Hardware Nodes", str(len(st.session_state.node_registry[v_name])), "Live Matrix")
    c3.metric("Power Draw", "840 kW", "Stable")
    st.divider()

    st.subheader("ASSET PROVISIONING & DECOMMISSIONING")
    prov1, prov2 = st.columns(2)
    with prov1:
        new_node = st.text_input("Commission New Hardware Node:", placeholder="e.g., DRONE-CHARLIE-03")
        if st.button("COMMISSION ASSET", type="primary"):
            if new_node and new_node not in st.session_state.node_registry[v_name]:
                st.session_state.node_registry[v_name].append(new_node)
                st.success(f"**ASSET COMMISSIONED:** `{new_node}` added to the operational matrix.")
                st.rerun()
    with prov2:
        if len(st.session_state.node_registry[v_name]) > 0:
            rem_node = st.selectbox("Decommission Hardware Node:", st.session_state.node_registry[v_name])
            if st.button("DECOMMISSION ASSET"):
                st.session_state.node_registry[v_name].remove(rem_node)
                st.error(f"**ASSET DECOMMISSIONED:** `{rem_node}` severed from the matrix.")
                st.rerun()
    st.divider()
    
    # --- HARDWIRED GRANULAR CONTROL MATRIX ---
    st.subheader("GRANULAR ASSET CONTROL (HARDWARE BRIDGE ACTIVE)")
    col1, col2, col3 = st.columns([1.5, 1, 1.5])
    
    with col1:
        st.markdown("**1. TARGET DESIGNATION**")
        active_fleet = st.session_state.node_registry[v_name] + ["TARGET ALL NODES"]
        target_node = st.selectbox("Isolate Specific Hardware:", active_fleet)
        
    with col2:
        st.markdown("**2. STATE TOGGLES**")
        state_pwr = st.toggle("Main Power Relay", value=True)
        state_vlv = st.toggle("Primary Actuator", value=False)
        
    with col3:
        st.markdown("**3. KINETIC PARAMETERS**")
        thrust_rpm = st.slider("Actuation Rate / Flow (%)", 0, 100, 35)
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("EXECUTE SURGICAL COMMAND", type="primary", use_container_width=True):
            if len(st.session_state.node_registry[v_name]) == 0 and target_node != "TARGET ALL NODES":
                 st.error("No active nodes to target.")
            else:
                with st.spinner("Broadcasting industrial payload to Edge Controllers..."):
                    time.sleep(0.4)
                    # THIS GENERATES THE ACTUAL PHYSICAL DATA PAYLOAD
                    hardware_payload = emit_kinetic_payload(v_name, target_node, state_pwr, state_vlv, thrust_rpm)
                
                st.success(f"**LOCKED:** Transmission successfully broadcast to `{target_node}`.")
                st.code(hardware_payload, language="json")

    st.divider()
    
    st.subheader("GLOBAL SECTOR OVERRIDES (EMERGENCY ONLY)")
    actions = verticals[v_name]
    a_cols = st.columns(len(actions))
    for idx, action in enumerate(actions):
        with a_cols[idx]:
            if st.button(action, use_container_width=True):
                st.error(f"**EXECUTED:** {action} protocol forced across {v_name}.")



