import streamlit as st
import time

st.set_page_config(page_title="EBONY | Live Command", layout="wide", initial_sidebar_state="expanded")

if 'role' not in st.session_state: st.session_state.role = 'GUEST'
if 'user' not in st.session_state: st.session_state.user = 'UNVERIFIED'

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Jon_Wilks_Shield.svg", width=100)
    st.markdown("### SOVEREIGN ACCESS")
    if st.session_state.role == 'GUEST':
        pwd = st.text_input("Sovereign Override", type="password")
        if st.button("Authenticate"):
            if pwd == "HVF2026!":
                st.session_state.role = 'CEO'
                st.session_state.user = 'JEFFERY HUMPHREY'
                st.rerun()
            elif pwd == "DREW2026!":
                st.session_state.role = 'COMMANDER'
                st.session_state.user = 'DREW'
                st.rerun()
            else:
                st.error("ACCESS DENIED.")
    else:
        st.success(f"Clearance: {st.session_state.role}")
        st.info(f"Operator: {st.session_state.user}")
        if st.button("Disengage"):
            st.session_state.role = 'GUEST'
            st.session_state.user = 'UNVERIFIED'
            st.rerun()
    
    st.markdown("---")
    st.markdown("**NODE STATUS:** ACTIVE")
    st.markdown("**UPLINK:** SECURE (UWB)")

st.markdown("## 🔴 EBONY: BARE-METAL COMMAND NODE")
st.markdown("---")

if st.session_state.role in ['CEO', 'COMMANDER']:
    st.success("STATUS: BARE-METAL UPLINK SECURED. LOCAL MESH TELEMETRY LIVE.")
    
    st.markdown("### 🌾 AGRICULTURE: SECTOR ALPHA")
    a1, a2, a3, a4 = st.columns(4)
    with a1: st.metric("Sector NDVI Vigor", "0.94", "+0.02", delta_color="normal")
    with a2: st.metric("Soil Matric Potential", "Optimal", "0 L/min flow")
    with a3: st.metric("Herd Biometrics", "Nominal", "0 Fevers")
    with a4: st.metric("Ag-Swarm Buffer", "12%", "-2% Load")
    
    st.markdown("---")
    st.markdown("### 🚛 LOGISTICS: SUPPLY CHAIN FLEET")
    l1, l2, l3, l4 = st.columns(4)
    with l1: st.metric("Fleet GPS Integrity", "100%", "0m Drift")
    with l2: st.metric("Sharded TSDB Ledger", "142K w/s", "Synced")
    with l3: st.metric("Cold Chain Pod A", "-18.0°C", "Stable")
    with l4: st.metric("AGV Dock Efficiency", "98%", "Optimal")
    
    st.markdown("---")
    st.markdown("### 🚁 DEFENSE: PERIMETER SECURITY")
    d1, d2, d3, d4 = st.columns(4)
    with d1: st.metric("Perimeter LiDAR", "CLEAR", "0 Anomalies")
    with d2: st.metric("Interceptor Swarm", "DOCKED", "Charging")
    with d3: st.metric("Biometric Vectors", "LOCKED", "Zero Spoofs")
    with d4: st.metric("Kinetic Gate Status", "SEALED", "Max Torque")

    st.markdown("---")
    st.markdown("### ⚡ KINETIC EXECUTION SWITCHES")
    st.warning("WARNING: Activating these switches will bypass autonomous loops and execute immediate physical reactions across the bare-metal mesh.")
    k1, k2, k3, k4 = st.columns(4)
    with k1: st.button("🚨 SCRAMBLE DEFENSE SWARM", use_container_width=True)
    with k2: st.button("💧 PURGE HYDRATION MAINS", use_container_width=True)
    with k3: st.button("🔒 FUSE PERIMETER GATES", use_container_width=True)
    with k4: st.button("☠️ TRIGGER KINETIC GUILLOTINE", use_container_width=True)

else:
    st.error("🔒 ACCESS DENIED. Executive clearance required to view live telemetry and operate kinetic execution switches.")
