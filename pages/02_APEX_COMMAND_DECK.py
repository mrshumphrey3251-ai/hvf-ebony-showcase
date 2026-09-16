import streamlit as st
import sys
import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

try:
    from core.hardware_bridge import emit_kinetic_payload
    from core.kinetic_parser import parse_kinetic_intent
    from core.rbac_matrix import evaluate_clearance, map_identity_to_tier
except ImportError:
    pass

st.set_page_config(page_title="EBONY // APEX COMMAND", layout="wide", initial_sidebar_state="expanded")

# --- ROOT IDENTITY VERIFICATION ---
if "active_identity" not in st.session_state:
    st.error("ACCESS DENIED. ROOT IDENTITY VERIFICATION REQUIRED.")
    st.stop()

# --- STEP-UP MFA GATE (SEAMLESS CALLBACK) ---
from core.mfa_matrix import verify_mfa_token

def verify_kinetic_callback():
    token = st.session_state.get("mfa_input_val", "")
    if verify_mfa_token(token, seed="EBONY_TIER_1_CEO") or verify_mfa_token(token, seed="EBONY_TIER_2_EXEC"):
        st.session_state.mfa_verified = True
    else:
        st.session_state.mfa_error = "ACCESS DENIED. INVALID KINETIC TOKEN."

if not st.session_state.get("mfa_verified", False):
    st.warning("⚠️ KINETIC SCADA OVERRIDE: CRYPTOGRAPHIC TOKEN REQUIRED FOR PHYSICAL ACTUATION.")
    st.text_input("Enter 6-Digit Sovereign MFA Token", type="password", key="mfa_input_val")
    st.button("VERIFY KINETIC CLEARANCE", type="primary", on_click=verify_kinetic_callback)
    if st.session_state.get("mfa_error"):
        st.error(st.session_state.mfa_error)
        del st.session_state.mfa_error
    st.stop()

# --- MAIN APEX DECK (AUTHENTICATED & SCADA CLEARED) ---
st.markdown("# 🦅 APEX COMMAND DECK")
st.caption("FUSED NEURAL & KINETIC ENGINE // ABSOLUTE DOMINANCE")

col_id, col_out = st.columns([4, 1])
with col_id:
    st.success(f"**ACTIVE CLEARANCE:** {st.session_state.active_identity}")
with col_out:
    if st.button("SEVER CONNECTION (LOGOUT)"):
        del st.session_state.active_identity
        if "mfa_verified" in st.session_state:
            del st.session_state.mfa_verified
        if "apex_history" in st.session_state:
            del st.session_state.apex_history
        st.rerun()
        
st.divider()

active_tier = map_identity_to_tier(st.session_state.active_identity)

if "apex_history" not in st.session_state:
    st.session_state.apex_history = []

for msg in st.session_state.apex_history:
    if msg["role"] == "payload":
        st.code(msg["content"], language="json")
    else:
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Issue Voice/Text Command...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.apex_history.append({"role": "user", "content": user_input})
    
    with st.spinner("Evaluating cryptographic clearance doors..."):
        time.sleep(0.5)
        
        kinetic_data = parse_kinetic_intent(user_input)
        
        if kinetic_data["intent_detected"]:
            action_severity = kinetic_data.get("action_severity", "KINETIC")
            clearance_check = evaluate_clearance(active_tier, action_severity)
            
            if clearance_check["access_granted"]:
                response = f"**{clearance_check['msg']}**\n\n**EXECUTION:** {kinetic_data['action_desc']}"
                st.chat_message("assistant").write(response)
                st.session_state.apex_history.append({"role": "assistant", "content": response})
                
                hardware_payload = emit_kinetic_payload(
                    kinetic_data["vertical"], 
                    kinetic_data["target_node"], 
                    kinetic_data["pwr_state"], 
                    kinetic_data["actuator_state"], 
                    kinetic_data["kinetic_rate"]
                )
                st.code(hardware_payload, language="json")
                st.session_state.apex_history.append({"role": "payload", "content": hardware_payload})
            else:
                st.chat_message("assistant").write(f"**{clearance_check['msg']}**")
                st.session_state.apex_history.append({"role": "assistant", "content": clearance_check["msg"]})
                
        else:
            if active_tier >= 4:
                 response = "ACCESS DENIED. GUEST CLEARANCE INSUFFICIENT FOR SOVEREIGN COMMUNICATION."
            else:
                 response = "Command received. No physical actuation detected. Omni-Matrix standing by."
                 
            st.chat_message("assistant").write(response)
            st.session_state.apex_history.append({"role": "assistant", "content": response})
