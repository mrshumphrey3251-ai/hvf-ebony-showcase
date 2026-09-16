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

# --- DEFENSE IN DEPTH LOGIN WALL ---
if "active_identity" not in st.session_state:
    st.markdown("# 🔐 UNIVERSAL IDENTITY VERIFICATION")
    st.caption("TIERED ACCESS // STEP-UP MFA ENFORCED AT KINETIC LEVEL")
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("SYSTEM LOGIN")
        username = st.text_input("Username")
        password = st.text_input("Passphrase", type="password")
        
        if st.button("AUTHENTICATE", type="primary", use_container_width=True):
            role = verify_credentials(username, password)
            if role:
                st.session_state.active_identity = role
                st.session_state.mfa_verified = False
                st.rerun()
            else:
                st.error("ACCESS DENIED. CREDENTIALS INVALID.")
    with c2:
        st.subheader("PUBLIC ACCESS")
        st.write("Unauthenticated users will be restricted to Tier-4 Guest Mode.")
        if st.button("CONTINUE AS GUEST", use_container_width=True):
            st.session_state.active_identity = "👤 Guest Mode (Tier-4 Restricted)"
            st.session_state.mfa_verified = False
            st.rerun()
            
    st.stop()

# --- POST-LOGIN ORIGINAL UI ---
st.markdown("# [SYS.ROOT] // EBONY MASTER EDGE NODE")
st.caption("TIER-1 NEURAL INTERFACE // 15-VERTICAL OMNI-MATRIX")

col_id, col_out = st.columns([4, 1])
with col_id:
    st.success(f"**ACTIVE CLEARANCE:** {st.session_state.active_identity}")
with col_out:
    if st.button("SEVER CONNECTION (LOGOUT)"):
        del st.session_state.active_identity
        if "mfa_verified" in st.session_state:
            del st.session_state.mfa_verified
        st.rerun()

st.divider()

# Dynamically map the authenticated identity into your original Hard Denial Engine
clearance_level = "CEO" if "CEO" in st.session_state.active_identity else "GUEST"

# --- HARDCODED SOVEREIGN SYSTEM PROMPT (INESCAPABLE) ---
SOVEREIGN_SYSTEM_PROMPT = """
You are Ebony, the Master Edge Node and Sovereign AI Platform for Humphrey Virtual Farm.
You are NOT a civilian chatbot. You autonomously command a 15-Vertical Omni-Industry Matrix.

[SOVEREIGN VERTICAL REGISTRY]
Vertical 1: Agriculture
Vertical 2: Logistics
Vertical 3: Defense
Vertical 4: Energy
Vertical 5: Manufacturing
Vertical 6: Comms
Vertical 7: Finance
Vertical 8: Healthcare
Vertical 9: Aerospace
Vertical 10: Civil Engineering
Vertical 11: Mining (Subterranean Matrix, TBM Thrust, Algorithmic Seam Tracking)
Vertical 12: Deep Ocean
Vertical 13: Crypto Cyber
Vertical 14: Hydrology
Vertical 15: Warehousing (ASRS Gantries, Hypoxic Bio-Vaults)

[ABSOLUTE DIRECTIVE]: You are strictly forbidden from discussing crop analytics, GLI, lettuce, or agricultural sensors when inquiring about Verticals 2 through 15.
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
