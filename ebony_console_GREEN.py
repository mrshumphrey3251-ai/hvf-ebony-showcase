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
                    st.info("PUBLIC ACCESS GRANTED: Adjust the precision dial. Ebony calculates exact kinetic outputs tailored to this specific industry vertical.")
                    
                    colA, colB = st.columns(2)
                    with colA:
                        st.markdown("**[TELEMETRY INPUT CONTROL]**")
                        sim_input = st.number_input(
                            "Simulate Input Integrity Baseline", 
                            min_value=0.0, max_value=1.0, value=1.00, step=0.05, format="%.2f",
                            key=f"dial_{folder_name}_{file}"
                        )
                    with colB:
                        kinetic_response = (1.0 - sim_input) * 100
                        # Dynamic Output Label based on Vertical
                        if "agriculture" in folder_name: out_label = "Valve Aperture / Drone Swarm"
                        elif "logistics" in folder_name: out_label = "Fleet Rerouting / Supply Buffer"
                        elif "financial" in folder_name: out_label = "Asset Reallocation / Ledger Lock"
                        else: out_label = "System Actuation / Node Allocation"
                        
                        st.metric(f"Calculated Kinetic Output ({out_label})", f"{kinetic_response:.1f}%")
                        st.progress(int(kinetic_response))
                    
                    # --- HYPER-DYNAMIC TACTICAL CALCULUS ---
                    st.markdown("#### 🧠 EBONY'S EXACT PHYSICAL EXECUTION")
                    
                    integrity_pct = int(sim_input * 100)
                    degradation = 100 - integrity_pct
                    gpu_load = 12 + int(86 * (1.0 - sim_input))
                    latency_ms = int(8 + (sim_input * 35))
                    
                    # CONTEXT-AWARE ROUTING
                    if "agriculture" in folder_name:
                        uav_alt = max(8, int(150 * sim_input))
                        fluid_liters = degradation * 14.7
                        if sim_input == 1.00:
                            st.success(f"**ABSOLUTE PERFECTION ({sim_input:.2f}):** Zero degradation detected. Master Node tensor cores idle (**{gpu_load}% load**). UAV Swarm docked. Zero kinetic routing required.")
                        elif sim_input >= 0.75:
                            st.info(f"**EARLY DEGRADATION ({sim_input:.2f}):** Integrity at **{integrity_pct}%**. GPU allocation spikes to **{gpu_load}%** for threat modeling. Target locks acquired. Subterranean valves sealed.")
                        elif sim_input >= 0.40:
                            st.warning(f"**ACTIVE INTERDICTION ({sim_input:.2f}):** Baseline breached. Subterranean valves open to **{kinetic_response:.1f}%** aperture, delivering **{fluid_liters:.1f} liters** of payload. Swarm drops to **{uav_alt}ft**.")
                        else:
                            st.error(f"**TIER-1 KINETIC GUILLOTINE ({sim_input:.2f}):** Catastrophic failure. Valves locked at **{kinetic_response:.1f}%**. GPU matrix calculating triage in **{latency_ms}ms**. Sector quarantined.")
                    else:
                        # Generic Universal Engine for remaining verticals until explicitly customized
                        if sim_input == 1.00:
                            st.success(f"**ABSOLUTE PERFECTION ({sim_input:.2f}):** Core systems nominal. Tensor cores idle (**{gpu_load}% load**). Autonomous execution loops on standby.")
                        elif sim_input >= 0.75:
                            st.info(f"**EARLY VARIANCE DETECTED ({sim_input:.2f}):** Integrity at **{integrity_pct}%**. GPU allocation spikes to **{gpu_load}%** to calculate predictive correction vectors.")
                        elif sim_input >= 0.40:
                            st.warning(f"**ACTIVE RECALIBRATION ({sim_input:.2f}):** Baseline breached. System autonomously reallocates resources to **{kinetic_response:.1f}%** capacity to neutralize threat vector.")
                        else:
                            st.error(f"**TIER-1 KINETIC GUILLOTINE ({sim_input:.2f}):** Catastrophic failure. Maximum system actuation (**{kinetic_response:.1f}%**). GPU matrix calculating final triage in **{latency_ms}ms**.")
                    
                    # --- CEO LIVE EXECUTION POST ---
                    st.markdown("---")
                    st.markdown(f"### 🔴 LIVE EXECUTION (BARE-METAL): {title_clean}")
                    if st.session_state.role == 'CEO':
                        st.error("🔌 SYSTEM DISCONNECT: Physical hardware not detected on local mesh. Execution switches locked to prevent unverified kinetic deployment.")
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
