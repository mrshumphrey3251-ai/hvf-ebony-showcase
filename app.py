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
                st.session_state.mfa_verified = False # Reset MFA state on new login
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

st.markdown("# [SYS.ROOT] // EBONY MASTER EDGE NODE")
st.success(f"**ACTIVE CLEARANCE:** {st.session_state.active_identity}")

if st.button("SEVER CONNECTION (LOGOUT)"):
    del st.session_state.active_identity
    if "mfa_verified" in st.session_state:
        del st.session_state.mfa_verified
    st.rerun()

st.divider()
st.info("OMNI-MATRIX UNLOCKED. SELECT A COMMAND MODULE FROM THE SIDEBAR.")
