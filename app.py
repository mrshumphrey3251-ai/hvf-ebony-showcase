import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from core.auth_matrix import verify_credentials
except ImportError:
    st.error("CRITICAL: REQUIRED CORE MODULES MISSING.")
    st.stop()

st.set_page_config(page_title="EBONY // MASTER BOOT", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR IDENTITY MATRIX (RESTORED LAYOUT) ---
st.sidebar.markdown("## 🔐 IDENTITY MATRIX")

if "active_identity" not in st.session_state:
    st.sidebar.caption("TIERED ACCESS REQUIRED")
    with st.sidebar.form("sidebar_login"):
        username = st.text_input("Username")
        password = st.text_input("Passphrase", type="password")
        submitted = st.form_submit_button("AUTHENTICATE", type="primary", use_container_width=True)
        
        if submitted:
            role = verify_credentials(username, password)
            if role:
                st.session_state.active_identity = role
                st.session_state.mfa_verified = False
                st.rerun()
            else:
                st.sidebar.error("ACCESS DENIED. CREDENTIALS INVALID.")
    
    if st.sidebar.button("CONTINUE AS GUEST", use_container_width=True):
        st.session_state.active_identity = "👤 Guest Mode (Tier-4 Restricted)"
        st.session_state.mfa_verified = False
        st.rerun()
else:
    st.sidebar.success(f"**ACTIVE CLEARANCE:**\n{st.session_state.active_identity}")
    if st.sidebar.button("SEVER CONNECTION (LOGOUT)", use_container_width=True):
        del st.session_state.active_identity
        if "mfa_verified" in st.session_state:
            del st.session_state.mfa_verified
        st.rerun()

st.sidebar.divider()
st.sidebar.caption("COMMAND MODULES:")
# Streamlit will dynamically render your pages/ list right below this line.

# --- MAIN PAGE: EBONY COMMS (RESTORED NEURAL INTERFACE) ---
st.markdown("# [SYS.ROOT] // EBONY MASTER EDGE NODE")
st.caption("TIER-1 NEURAL INTERFACE // 15-VERTICAL OMNI-MATRIX")
st.divider()

clearance_level = "CEO" if st.session_state.get("active_identity", "") and "CEO" in st.session_state.active_identity else "GUEST"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Command Ebony...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Processing sovereign directive..."):
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
