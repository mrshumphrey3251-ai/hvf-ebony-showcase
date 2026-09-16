import streamlit as st
import time
import random

st.set_page_config(page_title="EBONY // OMNI-MATRIX", layout="wide", initial_sidebar_state="collapsed")

# --- BARE-METAL HUD CSS INJECTION ---
st.markdown("""
<style>
    /* Force absolute dark mode and monospace terminal font */
    .stApp {
        background-color: #050505;
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3, h4, h5, h6, p, span, div {
        font-family: 'Courier New', Courier, monospace !important;
    }
    
    /* Executive Headers */
    h1 { color: #00FF41 !important; text-transform: uppercase; border-bottom: 2px solid #00FF41; padding-bottom: 10px; }
    h3 { color: #00BFFF !important; text-transform: uppercase; font-size: 1.1rem !important; margin-bottom: 5px; }
    
    /* Telemetry Metrics */
    [data-testid="stMetricValue"] { color: #00FF41 !important; font-weight: bold; }
    [data-testid="stMetricLabel"] { color: #A0A0A0 !important; font-size: 0.9rem !important; }
    
    /* Kinetic Action Buttons */
    .stButton>button {
        background-color: #050505 !important;
        border: 1px solid #00FF41 !important;
        color: #00FF41 !important;
        border-radius: 0px !important;
        font-weight: bold !important;
        transition: all 0.2s;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
        box-shadow: 0 0 10px #00FF41;
    }
    
    /* Primary Override Buttons (Red/Lethal) */
    button[kind="primary"] {
        border: 1px solid #FF003C !important;
        color: #FF003C !important;
    }
    button[kind="primary"]:hover {
        background-color: #FF003C !important;
        color: #000000 !important;
        box-shadow: 0 0 10px #FF003C;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("# [SYS.ROOT] // EBONY MASTER EDGE NODE")
st.caption("WARNING: TIER-1 EXECUTIVE OVERRIDE ACTIVE // UNRESTRICTED KINETIC ACCESS")

# --- 1. GLOBAL TELEMETRY MATRIX ---
st.markdown("### [ GLOBAL TELEMETRY DATASTREAM ]")
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("OPEX_BURN_RATE", "142.50 USD/HR", "OPT: -1.2%")
m2.metric("GRID_LOAD_MW", "12.40 MW", "ARB_ACTIVE")
m3.metric("AQUIFER_VOL", "4.2M GAL", "AWG_YIELD_MAX")
m4.metric("SWARM_SYNC", "100.0%", "LATENCY: 4ms")
m5.metric("CRYPTO_VAULT", "4.2M USD", "HASH: VALID")

st.markdown("<br><br>", unsafe_allow_html=True)

# --- 2. 15-VERTICAL KINETIC OVERRIDE VECTORS ---
st.markdown("### [ OMNI-MATRIX KINETIC OVERRIDES ]")

verticals = {
    "AGR_MATRIX": [{"label": "EXECUTE_PIVOT_ACTUATION", "type": "secondary", "msg": "TARGET ACQUIRED. PIVOTS KINETIC."}, {"label": "ENGAGE_FERTIGATION", "type": "primary", "msg": "NPK INJECTION VALVES OPEN."}],
    "LOG_MATRIX": [{"label": "REROUTE_AGV_SWARM", "type": "secondary", "msg": "PATHFINDING OVERRIDE ACKNOWLEDGED."}, {"label": "HARD_HALT_FLEET", "type": "primary", "msg": "KINETIC ASSETS IMMOBILIZED."}],
    "DEF_MATRIX": [{"label": "PERIMETER_SWEEP", "type": "secondary", "msg": "PATROL SWARM AIRBORNE."}, {"label": "AUTH_LETHAL_FORCE", "type": "primary", "msg": "WEAPONS HOT. ROE SUSPENDED."}],
    "NRG_MATRIX": [{"label": "DUMP_TO_GRID", "type": "secondary", "msg": "ARBITRAGE EXECUTING. INVOICING."}, {"label": "ISLAND_COMPOUND", "type": "primary", "msg": "CIVILIAN GRID SEVERED. SOVEREIGN MODE."}],
    "MFG_MATRIX": [{"label": "OVERDRIVE_SPINDLES", "type": "secondary", "msg": "CNC RPM CAPPED AT MAX_SAFE."}, {"label": "QUENCH_OVENS", "type": "primary", "msg": "NITROGEN FLOOD INITIATED."}],
    "COM_MATRIX": [{"label": "ROTATE_IP_TOPOLOGY", "type": "secondary", "msg": "SUBNET OBFUSCATION ACTIVE."}, {"label": "SEVER_FIBER_VHF", "type": "primary", "msg": "FIBER CUT. EMP-FALLBACK ONLINE."}],
    "FIN_MATRIX": [{"label": "FIRE_PROCUREMENT", "type": "secondary", "msg": "SMART CONTRACTS EXECUTED."}, {"label": "FREEZE_LIQUIDITY", "type": "primary", "msg": "FIAT SHIFTED TO COLD CRYPTO VAULT."}],
    "MED_MATRIX": [{"label": "DISPATCH_MED_UAV", "type": "secondary", "msg": "TRAUMA PACKAGE INBOUND."}, {"label": "BIOHAZARD_SEAL", "type": "primary", "msg": "HVAC ISOLATED. UV-C IGNITED."}],
    "AER_MATRIX": [{"label": "PULSE_PHASED_ARRAY", "type": "secondary", "msg": "RADAR SWEEPING HYPERSONIC BAND."}, {"label": "LAUNCH_INTERCEPTOR", "type": "primary", "msg": "HUNTER-KILLER VECTOR LOCKED."}],
    "CIV_MATRIX": [{"label": "HALT_3D_EXTRUSION", "type": "secondary", "msg": "CONCRETE GANTRY PAUSED."}, {"label": "FIRE_BASE_ISOLATORS", "type": "primary", "msg": "SEISMIC DAMPERS ACTUATED."}],
    "MIN_MATRIX": [{"label": "THROTTLE_TBM_THRUST", "type": "secondary", "msg": "BORING MACHINES AT 100%."}, {"label": "ABORT_SUBTERRANEAN", "type": "primary", "msg": "EVACUATING MINING SECTOR."}],
    "OCN_MATRIX": [{"label": "FEATHER_TURBINES", "type": "secondary", "msg": "TIDAL BLADES NEUTRALIZED."}, {"label": "FIRE_ACOUSTIC_SHOCK", "type": "primary", "msg": "HYDRO-DETERRENCE PULSE EMMITTED."}],
    "CYB_MATRIX": [{"label": "SPAWN_HONEYPOTS", "type": "secondary", "msg": "PHANTOM NODES ONLINE."}, {"label": "ZERO_DAY_WIPE", "type": "primary", "msg": "CRYPTOGRAPHIC VAULT INCINERATED."}],
    "HYD_MATRIX": [{"label": "OVERDRIVE_AWG", "type": "secondary", "msg": "CONDENSERS AT MAX YIELD."}, {"label": "LOCK_AQUIFER", "type": "primary", "msg": "SUBTERRANEAN VALVES SEALED."}],
    "WAR_MATRIX": [{"label": "PRE_KIT_PAYLOADS", "type": "secondary", "msg": "ASRS STAGING KINETIC GEAR."}, {"label": "VENT_HYPOXIC_GAS", "type": "primary", "msg": "NITROGEN PURGE. FIRE IMPOSSIBLE."}]
}

# Dynamically generate the bare-metal grid
vert_items = list(verticals.items())
cols_per_row = 5

for i in range(0, len(vert_items), cols_per_row):
    cols = st.columns(cols_per_row)
    for j, col in enumerate(cols):
        if i + j < len(vert_items):
            vert_name, controls = vert_items[i + j]
            with col:
                st.markdown(f"<div style='border:1px solid #333; padding:12px; margin-bottom:15px; background:#0a0a0a;'>", unsafe_allow_html=True)
                st.markdown(f"<span style='color:#00BFFF; font-weight:bold; font-size:1.1rem;'>[{vert_name}]</span>", unsafe_allow_html=True)
                st.markdown("<hr style='border-color: #333; margin-top: 5px; margin-bottom: 10px;'>", unsafe_allow_html=True)
                for ctrl in controls:
                    if st.button(ctrl["label"], key=f"{vert_name}_{ctrl['label']}", use_container_width=True, type=ctrl["type"]):
                        # Simulate hex handshake
                        with st.spinner(f"TX_HASH: {hex(random.randint(0x100000, 0xFFFFFF))}..."):
                            time.sleep(0.4) 
                        if ctrl["type"] == "primary":
                            st.markdown(f"<span style='color:#FF003C; font-weight:bold; font-size:0.8rem;'>[!] {ctrl['msg']}</span>", unsafe_allow_html=True)
                        else:
                            st.markdown(f"<span style='color:#00FF41; font-weight:bold; font-size:0.8rem;'>[+] {ctrl['msg']}</span>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
