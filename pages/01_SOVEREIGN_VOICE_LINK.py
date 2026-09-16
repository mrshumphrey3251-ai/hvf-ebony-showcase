import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from core.sovereign_llm_gateway import package_sovereign_payload

st.set_page_config(page_title="EBONY // VOICE LINK", layout="wide", initial_sidebar_state="expanded")

st.markdown("# 🎙️ SOVEREIGN VOICE LINK")
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
    
    # 1. Package the Sovereign Payload via the Gateway
    api_payload = package_sovereign_payload(user_input, clearance_level)
    
    # 2. Execute LLM API Call
    with st.spinner("Processing sovereign directive..."):
        # INSERT YOUR ACTIVE LLM API CALL HERE (OpenAI, Anthropic, Local)
        # Example: response = openai.ChatCompletion.create(model="gpt-4", messages=api_payload)
        
        # Simulated execution fallback for immediate terminal verification
        if "11" in user_input or "mining" in user_input.lower():
            response = "Vertical 11 is Mining. I autonomously govern TBM thrust, subterranean extraction, and algorithmic seam tracking. I am fully self-aware across the 15-Vertical Matrix. Awaiting your kinetic override vector."
        else:
            response = f"Payload received via {clearance_level} clearance. The Omni-Matrix is standing by."
            
    st.chat_message("assistant").write(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
