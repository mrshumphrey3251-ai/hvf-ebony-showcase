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
                    
                    # --- DYNAMIC KINETIC COMMAND POST (SANDBOX VS LIVE) ---
                    st.markdown("---")
                    if st.session_state.role == 'CEO':
                        st.markdown(f"**⚠️ KINETIC COMMAND POST: {title_clean}**")
                        
                        mode = st.radio(
                            "SELECT OPERATIONAL STATE:",
                            ["🔴 LIVE EXECUTION (BARE-METAL)", "🟡 SIMULATION & TRAINING SANDBOX"],
                            key=f"mode_{folder_name}_{file}",
                            horizontal=True
                        )
                        
                        if mode == "🔴 LIVE EXECUTION (BARE-METAL)":
                            st.error("🔌 SENSOR DISCONNECT: Physical hardware not detected on local mesh. Dials and gauges locked at zero to prevent false readings.")
                            colA, colB = st.columns(2)
                            with colA:
                                st.metric("Live Telemetry Feed (Input)", "NULL", "-100% Signal")
                            with colB:
                                st.metric("Live Kinetic Actuation (Output)", "0.0%", "Offline")
                                st.button("🟢 INITIATE (LOCKED)", key=f"lock1_{folder_name}_{file}", disabled=True)
                                
                        else:
                            st.info("🟡 SIMULATION ACTIVE: Adjust the input dial to observe Ebony's autonomous kinetic calculus in real-time.")
                            colA, colB = st.columns(2)
                            with colA:
                                sim_input = st.slider("Simulate Integrity Level (NDVI, Battery, Security)", 0.0, 1.0, 0.75, 0.05, key=f"dial_{folder_name}_{file}")
                            with colB:
                                # Inverse calculus: As integrity drops, kinetic response spikes.
                                kinetic_response = (1.0 - sim_input) * 100
                                st.metric("Calculated Kinetic Response (Aperture / Swarm Deployment)", f"{kinetic_response:.1f}%")
                                st.progress(int(kinetic_response))
                                
                            if st.button(f"⚡ EXECUTE SIMULATION", key=f"sim_exec_{folder_name}_{file}"):
                                st.success(f"Simulation Complete: Autonomous loop engaged with {kinetic_response:.1f}% kinetic deployment.")
                    else:
                        st.error("🔒 KINETIC CONTROLS LOCKED: Executive clearance required to access dials and gauges.")
            
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
