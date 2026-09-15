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

    # --- NATIVE STREAMLIT TABS (ZERO CSS HACKS) ---
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "🌾 Agriculture", 
        "🚛 Logistics", 
        "🚁 Defense", 
        "⚡ Energy",
        "🏭 Manufacturing",
        "📡 Comms",
        "🏦 Finance",
        "🏥 Healthcare",
        "🛰️ Aerospace"
    ])

    # Efficient Loader Engine: Prevents code bloat when rendering SITREPs
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
                st.info(f"Pillars are currently being forged for {folder_name.upper()}.")
        else:
            st.error(f"CRITICAL: Directory missing -> {folder_path}")

    # Map the tabs to their physical backend directories
    with tab1: load_vertical("01_sovereign_agriculture")
    with tab2: load_vertical("02_logistics_and_supply_chain")
    with tab3: load_vertical("03_defense_tactical")
    with tab4: load_vertical("04_distributed_energy_grid")
    with tab5: load_vertical("05_advanced_manufacturing")
    with tab6: load_vertical("06_secure_communications")
    with tab7: load_vertical("07_financial_ledger_autonomy")
    with tab8: load_vertical("08_edge_healthcare_bio_metrics")
    with tab9: load_vertical("09_aerospace_perimeter_telemetry")