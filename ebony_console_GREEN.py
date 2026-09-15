import streamlit as st
import os

st.set_page_config(page_title="Humphrey Virtual Farm | Ebony Command", page_icon="⚡", layout="wide")

# --- STABLE SIDEBAR: ADA VOICE, OPSEC & ACCESS PORTAL ---
st.sidebar.markdown("### 🎙️ ADA Voice Link")
st.sidebar.button("Tap to speak (Must say 'Ebony')")
st.sidebar.text("00:00")
st.sidebar.markdown("---")

st.sidebar.markdown("### 🛡️ Presentation OPSEC")
st.sidebar.checkbox("Activate Demo Mode (Mask Secrets)")
st.sidebar.selectbox("Select Active Engine:", ["👤 Guest Mode", "CEO Clearance"])

st.sidebar.markdown("### Access Portal:")
st.sidebar.text_input("Username:")
st.sidebar.text_input("Password:", type="password")
st.sidebar.markdown("---")

# --- COMMAND MODULES NAVIGATION ---
st.sidebar.title("🎛️ Command Modules")
menu = ["⚡ Command Deck", "📘 OMNI-INDUSTRY MATRIX"]
choice = st.sidebar.radio("Navigate:", menu)

# --- MAIN SCREEN ROUTING ---
if choice == "⚡ Command Deck":
    st.title("⚡ Humphrey Virtual Farm Command Deck | Ebony AI")
    st.markdown("**Active User:** CEO | 🛡️ **Mode:** 🟢 Online (Cloud Fast Link)")
    st.info("System is operating at Tier-1 Sovereign Capacity.")

elif choice == "📘 OMNI-INDUSTRY MATRIX":
    st.title("📘 OMNI-INDUSTRY MATRIX")

    # --- NATIVE 15-VERTICAL ARRAY ---
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

    # Generate the 15 tabs natively
    tabs = st.tabs([v[0] for v in verticals])

    # Efficient Loader Engine
    def load_vertical(folder_name):
        folder_path = os.path.join("docs", folder_name)
        if os.path.exists(folder_path):
            md_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
            if md_files:
                for md_file in md_files:
                    title = md_file.replace(".md", "").replace("_", " ").upper()
                    with st.expander(f"📘 {title}"):
                        with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                            st.markdown(f.read())
            else:
                st.info("Pillars are currently being forged for this Sovereign Vertical.")
        else:
            st.error(f"CRITICAL: Directory missing -> {folder_path}")

    # Map the tabs to their physical backend directories
    for i, tab in enumerate(tabs):
        with tab:
            load_vertical(verticals[i][1])
