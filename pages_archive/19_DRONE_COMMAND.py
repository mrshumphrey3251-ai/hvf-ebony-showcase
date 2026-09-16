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
    st.stop()# --- 🌾 DRONE DIAGNOSTICS ---
st.markdown("### 🚁 /// OPTICAL PAYLOAD FEED (LIVE & GLI ACTIVE)")
run_camera = st.checkbox("[ ARM OPTICAL LINK WITH GLI ]", key="master_cam_toggle")
FRAME_WINDOW = st.image([])

if run_camera:
    import cv2
    import numpy as np
    try:
        camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        if not camera.isOpened():
            camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while run_camera:
            ret, frame = camera.read()
            if not ret: break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            r_img, g_img, b_img = cv2.split(frame_rgb.astype(np.float32))

            denominator = (2 * g_img + r_img + b_img)
            denominator[denominator == 0] = 1
            gli_matrix = (2 * g_img - r_img - b_img) / denominator
            avg_gli = np.mean(gli_matrix)

            st.session_state["last_gli"] = float(avg_gli)

            cv2.putText(frame_rgb, "EBONY OPTICAL: ACTIVE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            gli_color = (0, 255, 0) if avg_gli > 0.1 else (255, 0, 0)
            cv2.putText(frame_rgb, f"LIVE GLI SCORE: {avg_gli:.3f}", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.8, gli_color, 2)

            FRAME_WINDOW.image(frame_rgb)
        camera.release()
    except Exception as e:
        st.error(f"HARDWARE INTERLOCK FAILURE: {e}")
else:
    st.info("[!] OPTICAL PAYLOAD OFFLINE. AWAITING CEO OVERRIDE.")

if "last_gli" in st.session_state:
    st.markdown("---")
    st.markdown("### 🧠 /// NEURAL BRIDGE: AI INGESTION")
    if st.button("[ TRANSMIT TELEMETRY TO AI CORE ]"):
        gli_val = st.session_state["last_gli"]
        st.success(f"TELEMETRY CAPTURED: GLI = {gli_val:.3f}. Transmitted to Neural Core.")

st.subheader("🌾 Aerial Ingest")
drone_linked = st.toggle("📡 Arm Drone Feed (Simulate Active RTMP Handshake)", value=False)
WEBRTC_STREAM_URL = "http://192.168.1.175:8889/live/stream"

if drone_linked:
    st.components.v1.html(f'<iframe src="{WEBRTC_STREAM_URL}" width="100%" height="450" frameborder="0" allowfullscreen></iframe>', height=470)
    st.success("🟢 LIVE: Universal Drone Ingest Active")
else:
    st.markdown("### 🔴 No Active Craft Detected")
    local_vid_path = os.path.join(REPO_DIR, "drone_training.mp4")
    if os.path.exists(local_vid_path):
        st.video(local_vid_path, loop=True, autoplay=True, muted=True)
    else:
        st.video("https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4", loop=True, autoplay=True, muted=True)
