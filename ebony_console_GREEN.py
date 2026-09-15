import streamlit as st
import os

st.set_page_config(page_title="Humphrey Virtual Farm | Ebony Command", page_icon="⚡", layout="wide")

# APEX STANDARD: Force 15-Vertical Matrix Tabs into Multi-Row Layout
st.markdown("""
    <style>
    /* Force Streamlit Tabs to wrap into multiple rows */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        flex-wrap: wrap;
    }
    /* Standardize tab sizing and text wrapping */
    .stTabs [data-baseweb="tab"] {
        flex-grow: 1;
        white-space: pre-wrap;
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🎛️ Command Modules")
st.sidebar.markdown("---")
menu = ["⚡ Command Deck", "📘 OMNI-INDUSTRY MATRIX (MASTERCLASS & BLUEPRINTS)"]
choice = st.sidebar.radio("Navigate:", menu)

# --- MAIN ROUTING ---
if choice == "⚡ Command Deck":
    st.title("⚡ Humphrey Virtual Farm Command Deck | Ebony AI")
    st.markdown("**Active User:** CEO | 🛡️ **Mode:** 🟢 Online (Cloud Fast Link)")
    st.info("System is operating at Tier-1 Sovereign Capacity.")

elif choice == "📘 OMNI-INDUSTRY MATRIX (MASTERCLASS & BLUEPRINTS)":
    # --- DYNAMIC 15-VERTICAL RENDERING ENGINE ---
    st.markdown("## 📘 OMNI-INDUSTRY MATRIX (MASTERCLASS & BLUEPRINTS)")

    # The 15 Sovereign Verticals Array
    verticals = [
        ("🌾 Agriculture", "01_sovereign_agriculture"),
        ("🚛 Logistics", "02_logistics_and_supply_chain"),
        ("🚁 Defense", "03_defense_tactical"),
        ("⚡ Energy", "04_distributed_energy_grid"),
        ("💧 Hydrology", "05_sovereign_hydrology"),
        ("🏭 Heavy Industry", "06_heavy_industry"),
        ("🏥 Biosecurity", "07_biosecurity"),
        ("🛰️ Aerospace", "08_aerospace"),
        ("🔐 Crypto Cyber", "09_cryptographic_cyber"),
        ("🏗️ Civil Eng.", "10_civil_engineering"),
        ("⛏️ Mining", "11_mining_extraction"),
        ("🌊 Deep Ocean", "12_deep_ocean"),
        ("🏦 Sovereign Finance", "13_sovereign_finance"),
        ("📡 Telecom", "14_sovereign_telecom"),
        ("📦 Warehousing", "15_autonomous_warehousing")
    ]

    # Autonomously generate the 15 multi-row tabs
    tabs = st.tabs([v[0] for v in verticals])

    # Loop through each tab and dynamically load its respective Markdown SITREPs
    for i, tab in enumerate(tabs):
        with tab:
            folder_path = os.path.join("docs", verticals[i][1])
            if os.path.exists(folder_path):
                md_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
                if md_files:
                    for md_file in md_files:
                        pillar_title = md_file.replace(".md", "").replace("_", " ").upper()
                        with st.expander(f"📘 {pillar_title}"):
                            with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                                st.markdown(f.read())
                else:
                    st.info("Pillars are currently being forged for this Sovereign Vertical.")
            else:
                st.error(f"CRITICAL: Directory missing -> {folder_path}")