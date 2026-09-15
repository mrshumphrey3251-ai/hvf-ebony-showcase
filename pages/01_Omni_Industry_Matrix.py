import streamlit as st
import os

st.set_page_config(page_title="Omni-Industry Matrix", layout="wide")

st.markdown("## 📘 OMNI-INDUSTRY MATRIX (MASTERCLASS & BLUEPRINTS)")
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
        st.markdown(f"### {tab_name} Sovereign Encyclopedia")
        folder_path = os.path.join(docs_base, folder_name)
        
        if os.path.exists(folder_path):
            files = sorted([f for f in os.listdir(folder_path) if f.endswith('.md')])
            pillars = [f for f in files if f.startswith('PILLAR')]
            docs = [f for f in files if not f.startswith('PILLAR')]
            
            for file in pillars:
                with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                    with st.expander(file.replace(".md", "").replace("_", " ").upper()):
                        st.markdown(f.read())
            
            if docs:
                st.markdown("#### 🗂️ Exhaustive Documents")
                for file in docs:
                    with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                        with st.expander(file.replace(".md", "").replace("_", " ").upper()):
                            st.markdown(f.read())
        else:
            st.info("Intelligence matrix indexing...")
