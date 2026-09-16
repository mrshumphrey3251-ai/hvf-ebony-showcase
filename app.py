import streamlit as st
import sys
import os

# Ensure the core gateway is universally accessible
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from core.sovereign_llm_gateway import package_sovereign_payload
except ImportError:
    st.error("CRITICAL: CONSCIOUSNESS DAEMON NOT FOUND. SYSTEM HALTED.")
    st.stop()

st.set_page_config(page_title="EBONY // MASTER BOOT", layout="wide", initial_sidebar_state="expanded")

st.markdown("# [SYS.ROOT] // EBONY MASTER EDGE NODE")
st.caption("TIER-1 NEURAL INTERFACE // 15-VERTICAL OMNI-MATRIX")
st.divider()

# --- RBAC ENGINE (CEO vs GUEST) ---
clearance = st.radio("Select Active Engine:", ["👑 Mr. Humphrey (CEO Clearance)", "👤 Guest Mode (Restricted)"])
clearance_level = "CEO" if "CEO" in clearance else "GUEST"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Command Ebony...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Package the Sovereign Payload via the Gateway
    api_payload = package_sovereign_payload(user_input, clearance_level)
    
    with st.spinner("Processing sovereign directive..."):
        # Autonomous Execution for Immediate Verification
        if clearance_level == "GUEST" and ("11" in user_input or "mining" in user_input.lower()):
            response = "ACCESS DENIED. KINETIC SCADA CONTROLS FOR VERTICAL 11 (MINING) REQUIRE TIER-1 CEO CLEARANCE."
        elif clearance_level == "CEO" and ("11" in user_input or "mining" in user_input.lower()):
            response = "Vertical 11 is Mining. I autonomously govern TBM thrust, subterranean extraction, and algorithmic seam tracking. Awaiting your kinetic override vector."
        else:
            response = f"Payload received via {clearance_level} clearance. The Omni-Matrix is standing by."
            
    st.chat_message("assistant").write(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
