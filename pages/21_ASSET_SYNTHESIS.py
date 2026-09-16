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
    st.stop()import requests
# --- 🎨 ASSET SYNTHESIS ---
st.subheader("🎨 Sovereign Image & Media Synthesis")
prompt = st.text_input("Enter Generation Prompt:", "High-tech executive handshake: HVF on left, SignalLink on right, Project Ebony banner centered", key="asset_prompt_input")
if st.button("Generate Sovereign Asset", use_container_width=True):
    with st.spinner("Synthesizing sovereign asset on local hardware..."):
        try:
            res = requests.post("http://localhost:8000/synthesis/image", params={"prompt": prompt}, headers={"x-auth-token": "CEO_OVERRIDE"})
            if res.status_code == 200:
                data = res.json()
                st.success(f"✅ {data.get('message')}")
                img_rel = data.get("image_path")
                img_file = os.path.join(REPO_DIR, img_rel) if img_rel else None
                if img_file and os.path.isfile(img_file):
                    st.image(img_file, caption="Sovereign Generated Asset | HVF Project Ebony Matrix", use_container_width=True)
            else:
                st.error(f"⚠️ Engine Error (HTTP {res.status_code})")
        except Exception as e:
            st.error(f"Matrix Offline: {e}")
