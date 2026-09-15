import streamlit as st
import os

st.set_page_config(page_title="Project Ebony | Master Edge Node", layout="wide")

# --- AUTHENTICATION ENGINE ---
if 'role' not in st.session_state:
    st.session_state.role = 'GUEST'

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Jon_Wilks_Shield.svg", width=100)
    st.markdown("### SOVEREIGN ACCESS")
    
    if st.session_state.role == 'GUEST':
        pwd = st.text_input("Executive Override", type="password")
        if st.button("Authenticate"):
            if pwd == "HVF2026!":
                st.session_state.role = 'CEO'
                st.rerun()
            else:
                st.error("Access Denied.")
    else:
        st.success("Clearance: MAXIMUM (CEO)")
        if st.button("Disengage"):
            st.session_state.role = 'GUEST'
            st.rerun()
            
    st.markdown("---")
    st.markdown("**STATUS:** System Operational")

# --- HORIZONTAL NAVIGATION (THE DOORS) ---
st.markdown("## 🌐 OMNI-INDUSTRY MATRIX")
st.markdown("---")

verticals = {
    "🌾 Agriculture": "01_sovereign_agriculture",
    "🚛 Logistics": "02_logistics_and_supply_chain",
    "🚁 Defense": "03_defense_tactical",
    "⚡ Energy": "04_distributed_energy_grid",
    "🦾 Manufacturing": "05_advanced_manufacturing",
    "🔐 Comms": "06_secure_communications",
    "📓 Financial": "07_financial_ledger_autonomy",
    "🫀 Healthcare": "08_edge_healthcare_bio_metrics",
    "🛰️ Aerospace": "09_aerospace_perimeter_telemetry"
}

tabs = st.tabs(list(verticals.keys()))
docs_base = r"C:\HVF_Repos\hvf-media-matrix-private\docs"

for idx, (tab_name, folder_name) in enumerate(verticals.items()):
    with tabs[idx]:
        st.markdown(f"### {tab_name} Command Architecture")
        folder_path = os.path.join(docs_base, folder_name)
        
        if os.path.exists(folder_path):
            files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
            pillars = [f for f in files if f.startswith('PILLAR')]
            docs = [f for f in files if not f.startswith('PILLAR')]
            
            # --- DROPDOWN: PILLARS & COMMAND POSTS ---
            st.markdown("#### 🏛️ Foundational Pillars & Tactical Command Posts")
            for file in pillars:
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                title_clean = file.replace(".md", "").replace("_", " ").upper()
                with st.expander(title_clean):
                    st.markdown(content)
                    
                    # --- PUBLIC SIMULATION SANDBOX ---
                    st.markdown("---")
                    st.markdown(f"### 🟡 SIMULATION & TRAINING SANDBOX: {title_clean}")
                    st.info("PUBLIC ACCESS GRANTED: Use the precision +/- buttons below to adjust the telemetry baseline. Observe Ebony's autonomous mathematical calculus and read the exact physical outcome she will execute.")
                    
                    colA, colB = st.columns(2)
                    with colA:
                        st.markdown("**[TELEMETRY INPUT CONTROL]**")
                        # Upgraded from slider to precision stepper
                        sim_input = st.number_input(
                            "Simulate Input Integrity (Health, Security, Battery)", 
                            min_value=0.0, 
                            max_value=1.0, 
                            value=0.85, 
                            step=0.05, 
                            format="%.2f",
                            key=f"dial_{folder_name}_{file}"
                        )
                    with colB:
                        kinetic_response = (1.0 - sim_input) * 100
                        st.metric("Calculated Kinetic Output (Valve Aperture / Drone Swarm Deployment)", f"{kinetic_response:.1f}%")
                        st.progress(int(kinetic_response))
                    
                    # DYNAMIC OUTCOME ANALYSIS
                    st.markdown("#### 🧠 EBONY'S KINETIC OUTCOME ANALYSIS")
                    if sim_input >= 0.75:
                        st.success(f"**STATUS OPTIMAL ({sim_input:.2f}):** The localized telemetry is within the Tier-1 acceptable baseline. Ebony passively logs this data to the secure ledger. Zero kinetic resources are deployed, preserving battery reserves and chemical payloads.")
                    elif sim_input >= 0.35:
                        st.warning(f"**STATUS DEGRADED ({sim_input:.2f}):** The integrity metric has fallen below optimal thresholds. Ebony autonomously routes investigative UAVs to the exact GPS coordinates to increase telemetry resolution. Underground hydration valves are primed but not yet opened.")
                    else:
                        st.error(f"**CRITICAL FAILURE DETECTED ({sim_input:.2f}):** The baseline has been breached. Ebony unilaterally triggers the Kinetic Guillotine protocol. Subterranean valves blast open to {kinetic_response:.1f}% capacity at the exact coordinates, and the defense swarm is scrambled for immediate intervention. Human authorization bypassed.")
                    
                    # --- CEO LIVE EXECUTION POST ---
                    st.markdown("---")
                    st.markdown(f"### 🔴 LIVE EXECUTION (BARE-METAL): {title_clean}")
                    if st.session_state.role == 'CEO':
                        st.error("🔌 SENSOR DISCONNECT: Physical hardware not detected on local mesh. Dials and gauges locked at zero to prevent false readings.")
                        colC, colD = st.columns(2)
                        with colC:
                            st.metric("Live Telemetry Feed (Input)", "NULL", "-100% Signal")
                        with colD:
                            st.metric("Live Kinetic Actuation (Output)", "0.0%", "Offline")
                            st.button("🟢 INITIATE (LOCKED)", key=f"lock1_{folder_name}_{file}", disabled=True)
                    else:
                        st.error("🔒 KINETIC CONTROLS LOCKED: Executive clearance required to access live bare-metal telemetry and execution switches.")
            
            # --- DROPDOWN: EXHAUSTIVE DOCS ---
            if docs:
                st.markdown("#### 🗂️ Exhaustive Documents")
                for file in docs:
                    file_path = os.path.join(folder_path, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    title_clean = file.replace(".md", "").replace("_", " ").upper()
                    with st.expander(title_clean):
                        st.markdown(content)
        else:
            st.info("Intelligence matrix indexing...")
