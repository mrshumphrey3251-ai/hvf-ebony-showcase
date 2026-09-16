import streamlit as st
import os

st.title("📘 OMNI-INDUSTRY MATRIX (MASTERCLASS & BLUEPRINTS)")
st.info("Sovereign 15-Vertical Tier-1 Architecture")

# --- NATIVE 15-VERTICAL ARRAY ---
verticals = [
    ("🌾 Agriculture", "01_sovereign_agriculture"),
    ("🚛 Logistics", "02_logistics_and_supply_chain"),
    ("🚁 Defense", "03_defense_tactical"),
    ("⚡ Energy", "04_distributed_energy_grid"),
    ("🏭 Manufacturing", "05_advanced_manufacturing"),
    ("📡 Comms", "06_secure_communications"),
    ("🏦 Finance", "07_financial_ledger_autonomy"),
    ("🏥 Healthcare", "08_edge_healthcare_bio_metrics"),
    ("🛰️ Aerospace", "09_aerospace_perimeter_telemetry"),
    ("🏗️ Civil Eng", "10_civil_engineering"),
    ("⛏️ Mining", "11_mining_extraction"),
    ("🌊 Deep Ocean", "12_deep_ocean"),
    ("🔐 Crypto Cyber", "13_cryptographic_cyber"),
    ("💧 Hydrology", "14_sovereign_hydrology"),
    ("📦 Warehousing", "15_autonomous_warehousing")
]

tabs = st.tabs([v[0] for v in verticals])

def load_vertical(folder_name):
    # Hard-locked to your master private vault to guarantee data consistency
    repo_dir = r"C:\HVF_Repos\hvf-media-matrix-private"
    folder_path = os.path.join(repo_dir, "docs", folder_name)
    
    if os.path.exists(folder_path):
        md_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
        if md_files:
            for md_file in md_files:
                title = md_file.replace(".md", "").replace("_", " ").upper()
                with st.expander(f"📘 {title}", expanded=False):
                    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                        st.markdown(f.read())
        else:
            st.info("Pillars are currently being forged for this Sovereign Vertical.")
    else:
        st.error(f"CRITICAL: Directory missing -> {folder_path}")

for i, tab in enumerate(tabs):
    with tab:
        load_vertical(verticals[i][1])
