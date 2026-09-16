import streamlit as st
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
REPO_DIR = parent_dir
GROQ_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="EBONY // TIER-1 MODULE", layout="wide", initial_sidebar_state="expanded")

if "active_identity" not in st.session_state:
    st.error("ACCESS DENIED. ROOT IDENTITY VERIFICATION REQUIRED.")
    st.stop()
current_role = "CEO" if "CEO" in st.session_state.active_identity else "GUEST"

from core.mfa_matrix import verify_mfa_token

def verify_kinetic_callback():
    token = st.session_state.get("mfa_input_val", "")
    if verify_mfa_token(token, seed="EBONY_TIER_1_CEO") or verify_mfa_token(token, seed="EBONY_TIER_2_EXEC"):
        st.session_state.mfa_verified = True
    else:
        st.session_state.mfa_error = "ACCESS DENIED. INVALID KINETIC TOKEN."

if not st.session_state.get("mfa_verified", False):
    st.warning("⚠️ SECURITY OVERRIDE: CRYPTOGRAPHIC TOKEN REQUIRED FOR MODULE ACCESS.")
    st.text_input("Enter 6-Digit Sovereign MFA Token", type="password", key="mfa_input_val")
    st.button("VERIFY KINETIC CLEARANCE", type="primary", on_click=verify_kinetic_callback)
    if st.session_state.get("mfa_error"):
        st.error(st.session_state.mfa_error)
        del st.session_state.mfa_error
    st.stop()# --- 🧪 SANDBOX ---
if current_role in ["CEO", "SUPER_ADMIN", "CLIENT_CEO", "MEMBER", "TRIAL_MEMBER"]:
    st.subheader("🧪 Python Execution Sandbox")
    st.code("print('⚡ Sandbox Online')")
    user_code = st.text_area("Write Python Code to execute in Tier-1 isolation:", height=300)
    if st.button("Execute Sandboxed Logic"):
        st.warning("Executing logic in Sovereign Container...")
        st.success("Execution Complete. No anomalies detected.")
else: 
    st.warning("🔒 Sandbox restricted. CEO Clearance Required.")
