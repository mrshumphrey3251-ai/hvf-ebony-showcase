import streamlit as st
import os

st.set_page_config(page_title="Humphrey Virtual Farm | Ebony Command", page_icon="⚡", layout="wide")

# --- SIDEBAR: ADA VOICE, OPSEC & ACCESS PORTAL ---
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
    
    # Restore the pristine 4-Vertical Native Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌾 Agriculture", 
        "🚛 Logistics", 
        "🚁 Defense", 
        "⚡ Energy"
    ])

    with tab1:
        folder_path = os.path.join("docs", "01_sovereign_agriculture")
        if os.path.exists(folder_path):
            for md_file in sorted([f for f in os.listdir(folder_path) if f.endswith('.md')]):
                title = md_file.replace(".md", "").replace("_", " ").upper()
                with st.expander(f"📘 {title}"):
                    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                        st.markdown(f.read())
                        
    with tab2:
        folder_path = os.path.join("docs", "02_logistics_and_supply_chain")
        if os.path.exists(folder_path):
            for md_file in sorted([f for f in os.listdir(folder_path) if f.endswith('.md')]):
                title = md_file.replace(".md", "").replace("_", " ").upper()
                with st.expander(f"📘 {title}"):
                    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                        st.markdown(f.read())
                        
    with tab3:
        folder_path = os.path.join("docs", "03_defense_tactical")
        if os.path.exists(folder_path):
            for md_file in sorted([f for f in os.listdir(folder_path) if f.endswith('.md')]):
                title = md_file.replace(".md", "").replace("_", " ").upper()
                with st.expander(f"📘 {title}"):
                    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                        st.markdown(f.read())
                        
    with tab4:
        folder_path = os.path.join("docs", "04_distributed_energy_grid")
        if os.path.exists(folder_path):
            for md_file in sorted([f for f in os.listdir(folder_path) if f.endswith('.md')]):
                title = md_file.replace(".md", "").replace("_", " ").upper()
                with st.expander(f"📘 {title}"):
                    with open(os.path.join(folder_path, md_file), "r", encoding="utf-8") as f:
                        st.markdown(f.read())