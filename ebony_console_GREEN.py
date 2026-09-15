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
                    st.info("PUBLIC ACCESS GRANTED: Adjust the precision dial. Ebony calculates exact GPU loads, drone altitudes, and fluid dynamics for every 0.05 increment.")
                    
                    colA, colB = st.columns(2)
                    with colA:
                        st.markdown("**[TELEMETRY INPUT CONTROL]**")
                        sim_input = st.number_input(
                            "Simulate Input Integrity (Health, Security, Battery)", 
                            min_value=0.0, max_value=1.0, value=1.00, step=0.05, format="%.2f",
                            key=f"dial_{folder_name}_{file}"
                        )
                    with colB:
                        kinetic_response = (1.0 - sim_input) * 100
                        st.metric("Calculated Kinetic Output (Valve Aperture / Drone Swarm)", f"{kinetic_response:.1f}%")
                        st.progress(int(kinetic_response))
                    
                    # --- HYPER-DYNAMIC TACTICAL CALCULUS ---
                    st.markdown("#### 🧠 EBONY'S EXACT PHYSICAL EXECUTION")
                    
                    # Dynamic physics calculated directly from the dial input
                    integrity_pct = int(sim_input * 100)
                    degradation = 100 - integrity_pct
                    uav_alt = max(8, int(150 * sim_input)) # Swarm drops lower as threat increases
                    gpu_load = 12 + int(86 * (1.0 - sim_input)) # Servers run hotter calculating triage
                    fluid_liters = degradation * 14.7 # Exact mathematical dosage
                    latency_ms = int(8 + (sim_input * 35)) # System speeds up as threat escalates
                    
                    if sim_input == 1.00:
                        st.success(f"**ABSOLUTE PERFECTION ({sim_input:.2f}):** Zero degradation detected. Ebony spins down Master Node tensor cores to idle (**{gpu_load}% load**) to conserve thermal energy. UAV Swarm is ordered to dock and trickle-charge. Zero kinetic routing required.")
                    elif sim_input >= 0.90:
                        st.success(f"**PEAK EFFICIENCY ({sim_input:.2f}):** Ebony detects a microscopic **{degradation}%** variance from mathematical perfection. Baseline calibrated. UAVs maintain high-altitude passive overwatch at **{uav_alt}ft**. Subterranean valves remain physically sealed.")
                    elif sim_input >= 0.75:
                        st.info(f"**EARLY DEGRADATION TRACKING ({sim_input:.2f}):** Integrity dropped to **{integrity_pct}%**. Ebony proactively spikes Edge Node GPU allocation to **{gpu_load}%** to run predictive threat modeling. No water deployed yet, but target locks are acquired on the exact coordinates.")
                    elif sim_input >= 0.60:
                        st.warning(f"**PREEMPTIVE TACTICAL STANCE ({sim_input:.2f}):** Noticeable stress vector detected. Ebony autonomously drops UAV swarm altitude to **{uav_alt}ft** for high-resolution thermal scanning. Underground mainlines are pressurized. Routing execution latency locked at **{latency_ms}ms**.")
                    elif sim_input >= 0.40:
                        st.warning(f"**ACTIVE THREAT INTERDICTION ({sim_input:.2f}):** Baseline officially breached. Ebony unilaterally cracks subterranean valves to **{kinetic_response:.1f}%** aperture, mathematically calculating and delivering exactly **{fluid_liters:.1f} liters** of kinetic payload. GPU load spiked to **{gpu_load}%**.")
                    elif sim_input >= 0.20:
                        st.error(f"**CRITICAL ASSET STABILIZATION ({sim_input:.2f}):** Severe sector trauma. Ebony opens valves to **{kinetic_response:.1f}%**. Drone swarm deployed in micro-hover (**{uav_alt}ft**) to continuously monitor chemical saturation. Human authorization bypassed to prevent total asset loss.")
                    elif sim_input > 0.00:
                        st.error(f"**TIER-1 KINETIC GUILLOTINE ({sim_input:.2f}):** Catastrophic failure impending. Ebony executes maximum resource dump. Valves locked at **{kinetic_response:.1f}%**. GPU matrix running at **{gpu_load}%** load calculating triage vectors in **{latency_ms}ms**. Immediate physical intervention by CEO advised.")
                    else:
                        st.error(f"**SECTOR DEATH - CONTAINMENT PROTOCOL ({sim_input:.2f}):** Asset is mathematically unsalvageable. Ebony has autonomously severed hydration to this grid to protect remaining sovereign reserves. Kinetic Guillotine engaged. Sector quarantined.")
                    
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
