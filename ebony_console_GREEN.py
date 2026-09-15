import streamlit as st
import os

st.set_page_config(page_title="Project Ebony | Master Edge Node", layout="wide")

if 'role' not in st.session_state: st.session_state.role = 'GUEST'

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

st.markdown("## 🌐 OMNI-INDUSTRY MATRIX")
st.markdown("---")

verticals = {
    "🌾 Agriculture": "01_sovereign_agriculture",
    "🚛 Logistics": "02_logistics_and_supply_chain",
    "🚁 Defense": "03_defense_tactical",
    "⚡ Energy": "04_distributed_energy_grid"
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
                    
                    is_ag = "agriculture" in folder_name.lower()
                    is_log = "logistics" in folder_name.lower()
                    
                    # HARDCODED ROUTING
                    if is_ag and "PILLAR_1" in file.upper(): sim_label, out_label = "Simulate Crop Health (NDVI)", "Chemical Output Request"
                    elif is_ag and "PILLAR_2" in file.upper(): sim_label, out_label = "Simulate Swarm Bandwidth", "Buffer Back-Pressure Applied"
                    elif is_ag and "PILLAR_3" in file.upper(): sim_label, out_label = "Simulate Authorization Integrity", "Valve Lockdown Force"
                    elif is_ag and "PILLAR_4" in file.upper(): sim_label, out_label = "Simulate Soil Matric Potential", "Emitter Flow Rate (L/min)"
                    elif is_ag and "PILLAR_5" in file.upper(): sim_label, out_label = "Simulate Pathogen Threat Level", "Eradication Protocol Intensity"
                    elif is_ag and "PILLAR_6" in file.upper(): sim_label, out_label = "Simulate Biomass Growth", "Predictive Harvest Shift"
                    elif is_ag and "PILLAR_7" in file.upper(): sim_label, out_label = "Simulate Audit Standard", "Hashing Speed"
                    elif is_ag and "PILLAR_8" in file.upper(): sim_label, out_label = "Simulate Herd Thermal Health", "Quarantine Gate Actuation"
                    elif is_ag and "PILLAR_9" in file.upper(): sim_label, out_label = "Simulate Engine Vibration", "Predictive Torque Throttling"
                    elif is_log and "PILLAR_1" in file.upper(): sim_label, out_label = "Simulate GPS Signal Integrity", "Dead Reckoning Actuation"
                    elif is_log and "PILLAR_2" in file.upper(): sim_label, out_label = "Simulate Network Write Stability", "Local Shard Fallback"
                    elif is_log and "PILLAR_3" in file.upper(): sim_label, out_label = "Simulate Perimeter Geo-Fence", "Kinetic Gate Lockdown Force"
                    elif is_log and "PILLAR_4" in file.upper(): sim_label, out_label = "Simulate Cargo Thermal Variance", "Compressor Actuation (kW)"
                    elif is_log and "PILLAR_5" in file.upper(): sim_label, out_label = "Simulate Dock Efficiency", "AGV Swarm Reallocation"
                    elif is_log and "PILLAR_6" in file.upper(): sim_label, out_label = "Simulate Drivetrain Fatigue", "Fleet Throttling / Grounding"
                    elif is_log and "PILLAR_7" in file.upper(): sim_label, out_label = "Simulate Network Handoff", "Handshake Latency"
                    elif is_log and "PILLAR_8" in file.upper(): sim_label, out_label = "Simulate Route Hostility", "Asset Denial Protocol"
                    elif is_log and "PILLAR_9" in file.upper(): sim_label, out_label = "Simulate Cargo Mass Variance", "Payload Calibration"
                    else: sim_label, out_label = "Simulate Integrity", "System Actuation"
                    
                    st.markdown("---")
                    st.markdown(f"### 🟡 SIMULATION & TRAINING SANDBOX: {title_clean}")
                    st.info("PUBLIC ACCESS GRANTED: Adjust the precision dial to observe Ebony's mathematical execution.")
                    
                    colA, colB = st.columns(2)
                    with colA:
                        sim_input = st.number_input(sim_label, min_value=0.0, max_value=1.0, value=1.00, step=0.05, format="%.2f", key=f"dial_{folder_name}_{file}")
                    with colB:
                        kinetic_response = (1.0 - sim_input) * 100
                        st.metric(f"Calculated Output ({out_label})", f"{kinetic_response:.1f}%")
                        st.progress(int(kinetic_response))
                    
                    st.markdown("#### 🧠 EBONY'S EXACT PHYSICAL EXECUTION")
                    degradation = 100 - int(sim_input * 100)
                    gpu_load = 12 + int(86 * (1.0 - sim_input))
                    latency_ms = int(8 + (sim_input * 35))
                    
                    if is_ag and "PILLAR_1" in file.upper():
                        if sim_input >= 0.75: st.success("CROP VIGOR OPTIMAL: Infrared reflection perfect.")
                        else: st.error(f"YIELD COMPROMISED: Ebony routes {degradation * 14.7:.1f}L of chemical payload.")
                    elif is_ag and "PILLAR_2" in file.upper():
                        if sim_input >= 0.75: st.success("NETWORK CLEAR: 50 UAVs transmitting.")
                        else: st.error(f"OVERLOAD: Buffer full. {kinetic_response:.1f}% of UAVs grounded.")
                    elif is_ag and "PILLAR_3" in file.upper():
                        if sim_input >= 0.75: st.success("ZERO-TRUST SECURED.")
                        else: st.error("KINETIC GUILLOTINE FIRED: Node severed.")
                    elif is_ag and "PILLAR_4" in file.upper():
                        if sim_input >= 0.75: st.success("MOISTURE OPTIMAL.")
                        else: st.error(f"DROUGHT: Emitters blasting at {degradation * 0.45:.1f} L/min.")
                    elif is_ag and "PILLAR_5" in file.upper():
                        if sim_input >= 0.75: st.success("PERIMETER SECURE: Zero pathogens.")
                        else: st.error("INFESTATION CRITICAL: 100% Kinetic Eradication authorized.")
                    elif is_ag and "PILLAR_6" in file.upper():
                        if sim_input >= 0.75: st.success("YIELD TRAJECTORY NOMINAL.")
                        else: st.error(f"HARVEST COMPROMISED: Yield downgraded by {degradation * 1.8:.1f} tons.")
                    elif is_ag and "PILLAR_7" in file.upper():
                        if sim_input >= 0.75: st.success("ATTESTATION PERFECT.")
                        else: st.error("ATTESTATION FAILURE: Physical machinery halted.")
                    elif is_ag and "PILLAR_8" in file.upper():
                        if sim_input >= 0.75: st.success("HERD BIOMETRICS OPTIMAL.")
                        else: st.error(f"PATHOGEN VECTOR: Fever detected (+{degradation * 0.04:.1f}°C). Quarantine Gates snapped shut.")
                    elif is_ag and "PILLAR_9" in file.upper():
                        if sim_input >= 0.75: st.success("RESONANCE NOMINAL.")
                        else: st.error(f"FAILURE IMMINENT: Hard kill-switch executed. {kinetic_response:.1f}% power cut.")
                    
                    elif is_log and "PILLAR_1" in file.upper():
                        if sim_input >= 0.75: st.success(f"GPS OPTIMAL: Drift variance is {degradation * 0.4:.1f}m.")
                        elif sim_input >= 0.40: st.warning(f"SATELLITE DEGRADATION: Dead Reckoning bias applied. Drift corrected in {latency_ms}ms.")
                        else: st.error("SIGNAL LOSS: Master Node routing absolute trajectories via Dead Reckoning.")
                    elif is_log and "PILLAR_2" in file.upper():
                        if sim_input >= 0.75: st.success("LEDGER SYNC OPTIMAL.")
                        else: st.error("SYNC FAILURE: Ledger cached to isolated emergency NVMe drives.")
                    elif is_log and "PILLAR_3" in file.upper():
                        if sim_input >= 0.75: st.success("PERIMETER SECURE.")
                        else: st.error(f"KINETIC GATE INTERDICTION: Gates fused shut with {kinetic_response:.1f}% servo torque.")
                    elif is_log and "PILLAR_4" in file.upper():
                        if sim_input >= 0.75: st.success("COLD CHAIN NOMINAL.")
                        else: st.error(f"SPOILAGE THREAT: Emergency cooling units fired at {kinetic_response:.1f}%.")
                    elif is_log and "PILLAR_5" in file.upper():
                        if sim_input >= 0.75: st.success("DOCK GRID OPTIMAL.")
                        else: st.error(f"BOTTLENECK: {kinetic_response:.1f}% of transport fleet placed in holding pattern.")
                    elif is_log and "PILLAR_6" in file.upper():
                        if sim_input >= 0.75: st.success("DRIVETRAIN RESILIENCE OPTIMAL.")
                        else: st.error("PREVENTATIVE GROUNDING: Part fracture probability >98%. Ignition locked.")
                    elif is_log and "PILLAR_7" in file.upper():
                        if sim_input >= 0.75: st.success("HANDOFF SECURE.")
                        else: st.error(f"BLACKOUT TOLERANCE EXCEEDED: Hijack suspected. Engine killed with {kinetic_response:.1f}% force.")
                    elif is_log and "PILLAR_8" in file.upper():
                        if sim_input >= 0.75: st.success("ROUTE COMPLIANCE PERFECT.")
                        else: st.error("HIJACKING: Asset Denial triggered. Local memory wiped.")
                    elif is_log and "PILLAR_9" in file.upper():
                        if sim_input >= 0.75: st.success("PAYLOAD MASS VERIFIED.")
                        else: st.error(f"CRITICAL CARGO LOSS: {degradation * 45.5:.1f} lbs missing. Perimeter swarm deployed.")
                    
                    st.markdown("---")
                    st.markdown(f"### 🔴 LIVE EXECUTION (BARE-METAL): {title_clean}")
                    if st.session_state.role == 'CEO':
                        st.error("🔌 SENSOR DISCONNECT: Physical hardware not detected on local mesh.")
                        colC, colD = st.columns(2)
                        with colC: st.metric("Live Telemetry Feed (Input)", "NULL")
                        with colD:
                            st.metric("Live Kinetic Actuation (Output)", "0.0%")
                            st.button("🟢 INITIATE (LOCKED)", key=f"lock1_{folder_name}_{file}", disabled=True)
                    else:
                        st.error("🔒 KINETIC CONTROLS LOCKED: Executive clearance required.")
            
            if docs:
                st.markdown("#### 🗂️ Exhaustive Documents")
                for file in docs:
                    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                        with st.expander(file.replace(".md", "").replace("_", " ").upper()):
                            st.markdown(f.read())