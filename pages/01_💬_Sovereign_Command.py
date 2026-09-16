import streamlit as st
import os

st.markdown("# 💬 Sovereign Command // Ebony AI")
st.caption("TIER-1 NEURAL INTERFACE // OMNI-MATRIX")
st.divider()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "⚡ Sovereign AI online. Awaiting command."}]

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Command Ebony...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # KINETIC SECURITY: Chat logic executes freely, but sensitive API calls require identity
    if "active_identity" in st.session_state and "CEO" in st.session_state.active_identity:
        bot_reply = f"Payload received via Tier-1 CEO clearance: Processing directive '{user_input}' through Sovereign Engine."
    else:
        bot_reply = "GUEST MODE: Neural telemetry restricted. Please authenticate in the sidebar for full API access."
        
    st.chat_message("assistant").write(bot_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
