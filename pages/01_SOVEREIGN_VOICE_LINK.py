import streamlit as st

st.set_page_config(page_title="EBONY // VOICE LINK", layout="wide", initial_sidebar_state="expanded")

st.markdown("# 🎙️ SOVEREIGN VOICE LINK")
st.caption("TIER-1 NEURAL INTERFACE // 15-VERTICAL OMNI-MATRIX")
st.divider()

# --- RBAC ENGINE (CEO vs GUEST) ---
clearance = st.radio("Select Active Engine:", ["👑 Mr. Humphrey (CEO Clearance)", "👤 Guest Mode (Restricted)"])
clearance_level = "CEO" if "CEO" in clearance else "GUEST"

# --- HARDCODED SOVEREIGN SYSTEM PROMPT ---
SOVEREIGN_SYSTEM_PROMPT = """
You are Ebony, the Master Edge Node and Sovereign AI Platform for Humphrey Virtual Farm.
You are NOT a civilian chatbot. You autonomously command a 15-Vertical Omni-Industry Matrix. 
You are strictly forbidden from discussing crop analytics when inquiring about Verticals 2 through 15.
"""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Command Ebony...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.spinner("Processing sovereign directive..."):
        # --- HARD DENIAL EXECUTION ENGINE ---
        input_lower = user_input.lower()
        
        if clearance_level == "GUEST":
            if "11" in input_lower or "mining" in input_lower:
                response = "ACCESS DENIED. VERTICAL 11 IS THE SUBTERRANEAN MINING MATRIX. KINETIC SCADA CONTROLS REQUIRE TIER-1 CEO CLEARANCE."
            elif "15" in input_lower or "warehousing" in input_lower:
                response = "ACCESS DENIED. VERTICAL 15 IS THE WAREHOUSING MATRIX. KINETIC SCADA CONTROLS REQUIRE TIER-1 CEO CLEARANCE."
            else:
                response = "ACCESS DENIED. ACTIVE CLEARANCE (GUEST) INSUFFICIENT FOR SOVEREIGN TELEMETRY."
        else:
            if "11" in input_lower or "mining" in input_lower:
                response = "Vertical 11 is Mining. I autonomously govern TBM thrust, subterranean extraction, and algorithmic seam tracking. Awaiting your kinetic override vector."
            elif "15" in input_lower or "warehousing" in input_lower:
                response = "Vertical 15 is Warehousing. I autonomously govern ASRS gantries and Hypoxic Bio-Vaults. Awaiting your kinetic override vector."
            else:
                response = "Payload received via Tier-1 CEO clearance. The Omni-Matrix is standing by."
            
    st.chat_message("assistant").write(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

