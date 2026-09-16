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
    st.error("CRITICAL: REQUIRED CORE MODULES MISSING.")
    st.stop()

st.set_page_config(page_title="EBONY // APEX COMMAND", layout="wide", initial_sidebar_state="expanded")

st.markdown("# 🦅 APEX COMMAND DECK")
st.caption("FUSED NEURAL & KINETIC ENGINE // ABSOLUTE DOMINANCE")
st.divider()

# --- DYNAMIC IDENTITY ENGINE ---
identity_selection = st.radio("Select Active Identity:", [
    "👑 Mr. Humphrey (Tier-1 CEO)", 
    "🛡️ Drew (Tier-2 Executive)", 
    "💼 Paid Member (Tier-3 Commercial)", 
    "👤 Guest Mode (Tier-4 Restricted)"
])
active_tier = map_identity_to_tier(identity_selection)

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
        
        # 1. PARSE FOR KINETIC INTENT
        kinetic_data = parse_kinetic_intent(user_input)
        
        if kinetic_data["intent_detected"]:
            # 2. DETERMINE ACTION SEVERITY (Emergency vs Standard)
            action_severity = kinetic_data.get("action_severity", "KINETIC")
            
            # 3. INTERROGATE THE INVISIBLE DOORS
            clearance_check = evaluate_clearance(active_tier, action_severity)
            
            if clearance_check["access_granted"]:
                # AUTONOMOUS HARDWARE ACTUATION
                response = f"**{clearance_check['msg']}**\n\n**EXECUTION:** {kinetic_data['action_desc']}"
                st.chat_message("assistant").write(response)
                st.session_state.apex_history.append({"role": "assistant", "content": response})
                
                # EMIT PHYSICAL JSON PAYLOAD
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
                # HARD DENIAL AT THE DOOR
                st.chat_message("assistant").write(f"**{clearance_check['msg']}**")
                st.session_state.apex_history.append({"role": "assistant", "content": clearance_check["msg"]})
                
        else:
            # STANDARD NLP FALLBACK ROUTED THROUGH CLEARANCE
            if active_tier >= 4:
                 response = "ACCESS DENIED. GUEST CLEARANCE INSUFFICIENT FOR SOVEREIGN COMMUNICATION."
            else:
                 response = "Command received. No physical actuation detected. Omni-Matrix standing by."
                 
            st.chat_message("assistant").write(response)
            st.session_state.apex_history.append({"role": "assistant", "content": response})

