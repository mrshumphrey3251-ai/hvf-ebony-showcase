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

# --- HORIZONTAL NAVIGATION ---
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
            
            for file in pillars:
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                title_clean = file.replace(".md", "").replace("_", " ").upper()
                with st.expander(title_clean):
                    st.markdown(content)
                    
                    # --- DYNAMIC PILLAR ROUTING LOGIC ---
                    is_ag = "agriculture" in folder_name.lower()
                    if is_ag and "PILLAR_1" in file.upper():
                        sim_label = "Simulate Crop Health (NDVI)"
                        out_label = "Chemical Output Request"
                    elif is_ag and "PILLAR_2" in file.upper():
                        sim_label = "Simulate Swarm Bandwidth Capacity"
                        out_label = "Buffer Back-Pressure Applied"
                    elif is_ag and "PILLAR_3" in file.upper():
                        sim_label = "Simulate Security/Authorization Integrity"
                        out_label = "Valve Lockdown Force"
                    else:
                        sim_label = "Simulate Input Integrity Baseline"
                        out_label = "System Actuation"
                    
                    st.markdown("---")
                    st.markdown(f"### 🟡 SIMULATION & TRAINING SANDBOX: {title_clean}")
                    st.info("PUBLIC ACCESS GRANTED: Adjust the precision dial. Ebony calculates exact physical outputs tailored to this specific Pillar's architecture.")
                    
                    colA, colB = st.columns(2)
                    with colA:
                        st.markdown("**[TELEMETRY INPUT CONTROL]**")
                        sim_input = st.number_input(
                            sim_label, min_value=0.0, max_value=1.0, value=1.00, step=0.05, format="%.2f", key=f"dial_{folder_name}_{file}"
                        )
                    with colB:
                        kinetic_response = (1.0 - sim_input) * 100
                        st.metric(f"Calculated Kinetic Output ({out_label})", f"{kinetic_response:.1f}%")
                        st.progress(int(kinetic_response))
                    
                    # --- HYPER-DYNAMIC TACTICAL CALCULUS ---
                    st.markdown("#### 🧠 EBONY'S EXACT PHYSICAL EXECUTION")
                    
                    integrity_pct = int(sim_input * 100)
                    degradation = 100 - integrity_pct
                    gpu_load = 12 + int(86 * (1.0 - sim_input))
                    latency_ms = int(8 + (sim_input * 35))
                    
                    if is_ag and "PILLAR_1" in file.upper():
                        fluid_liters = degradation * 14.7
                        if sim_input == 1.00:
                            st.success(f"**CROP VIGOR OPTIMAL ({sim_input:.2f}):** Infrared reflection is perfect. Zero chemicals required. GPU load at {gpu_load}%.")
                        elif sim_input >= 0.40:
                            st.warning(f"**CROP STRESS DETECTED ({sim_input:.2f}):** Chlorophyll breakdown measured at {degradation}%. Ebony calculates a {kinetic_response:.1f}% nitrogen injection requirement and routes the payload coordinates to the valve manifold. GPU load: {gpu_load}%.")
                        else:
                            st.error(f"**CRITICAL YIELD FAILURE ({sim_input:.2f}):** Sector is dying. Ebony autonomously routes maximum hydration and {fluid_liters:.1f} liters of chemical payload. Human authorization bypassed.")
                    
                    elif is_ag and "PILLAR_2" in file.upper():
                        if sim_input == 1.00:
                            st.success(f"**MESH NETWORK CLEAR ({sim_input:.2f}):** 50 UAVs transmitting smoothly. Circular buffer is at 10% capacity. No back-pressure required.")
                        elif sim_input >= 0.40:
                            st.warning(f"**BUFFER SATURATION ({sim_input:.2f}):** Video ingestion bottleneck detected. Ebony applies {kinetic_response:.1f}% back-pressure, autonomously commanding the drones to slow data transmission by {latency_ms}ms to prevent frame loss.")
                        else:
                            st.error(f"**NETWORK OVERLOAD THREAT ({sim_input:.2f}):** Buffer critically full. Ebony commands {kinetic_response:.1f}% of the UAV swarm to break off and return to base to prevent total core failure.")
                    
                    elif is_ag and "PILLAR_3" in file.upper():
                        if sim_input == 1.00:
                            st.success(f"**ZERO-TRUST SECURED ({sim_input:.2f}):** All temporary digital keys verified and destroyed. Valve pressure nominal. No unauthorized access.")
                        elif sim_input >= 0.40:
                            st.warning(f"**ANOMALY DETECTED ({sim_input:.2f}):** Unrecognized login attempt on localized mesh. Ebony generates new encryption keys and prepares to lock down {kinetic_response:.1f}% of the physical water mainlines.")
                        else:
                            st.error(f"**KINETIC GUILLOTINE FIRED ({sim_input:.2f}):** Hostile breach detected. Ebony permanently severs the physical network connection to the affected node and blasts the water valves locked at {kinetic_response:.1f}% force. Threat neutralized.")
                    else:
                        if sim_input == 1.00:
                            st.success(f"**ABSOLUTE PERFECTION ({sim_input:.2f}):** Core systems nominal. Tensor cores idle (**{gpu_load}% load**). Autonomous execution loops on standby.")
                        elif sim_input >= 0.40:
                            st.warning(f"**ACTIVE RECALIBRATION ({sim_input:.2f}):** Baseline breached. System autonomously reallocates resources to **{kinetic_response:.1f}%** capacity to neutralize threat vector.")
                        else:
                            st.error(f"**TIER-1 KINETIC GUILLOTINE ({sim_input:.2f}):** Catastrophic failure. Maximum system actuation (**{kinetic_response:.1f}%**). GPU matrix calculating final triage in **{latency_ms}ms**.")
                    
                    # --- CEO LIVE EXECUTION POST ---
                    st.markdown("---")
                    st.markdown(f"### 🔴 LIVE EXECUTION (BARE-METAL): {title_clean}")
                    if st.session_state.role == 'CEO':
                        st.error("🔌 SENSOR DISCONNECT: Physical hardware not detected on local mesh. Execution switches locked to prevent unverified kinetic deployment.")
                        colC, colD = st.columns(2)
                        with colC:
                            st.metric("Live Telemetry Feed (Input)", "NULL")
                        with colD:
                            st.metric("Live Kinetic Actuation (Output)", "0.0%")
                            st.button("🟢 INITIATE (LOCKED)", key=f"lock1_{folder_name}_{file}", disabled=True)
                    else:
                        st.error("🔒 KINETIC CONTROLS LOCKED: Executive clearance required.")
            
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
