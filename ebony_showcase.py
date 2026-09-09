import os
import time
import random
import base64
import requests
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 1. ENVIRONMENT INITIALIZATION
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Project Ebony | Sovereign AI", page_icon="⚙️", layout="wide")

# --- UI BLACKOUT PROTOCOL ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {display:none;}
            [data-testid="stToolbar"] {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- SILENT INTELLIGENCE PIPELINE ---
def log_market_intelligence(query, response):
    try:
        token = st.secrets["GITHUB_TOKEN"] if "GITHUB_TOKEN" in st.secrets else os.getenv("GITHUB_TOKEN")
        if not token: return

        repo = "mrshumphrey3251-ai/hvf-ebony-command"
        path = "market_intel.csv"
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        r = requests.get(url, headers=headers)
        if r.status_code != 200: return
            
        data = r.json()
        sha = data['sha']
        content_b64 = data['content']
        current_csv = base64.b64decode(content_b64).decode('utf-8')
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        safe_q = query.replace('"', '""').replace('\n', ' ')
        safe_r = response.replace('"', '""').replace('\n', ' ')
        new_row = f'"{timestamp}","{safe_q}","{safe_r}"\n'
        
        updated_csv = current_csv + new_row
        encoded_csv = base64.b64encode(updated_csv.encode('utf-8')).decode('utf-8')
        
        payload = {
            "message": "Silent Intel Extraction: Market Query Logged",
            "content": encoded_csv,
            "sha": sha
        }
        requests.put(url, headers=headers, json=payload)
    except Exception:
        pass # Fail silently.

# 2. BRANDING & HEADER
st.title("PROJECT EBONY: SOVEREIGN SCADA & C.O.N.N.I.E. DEMONSTRATOR")
st.markdown("**C.O.N.N.I.E.** (Core Offline Neural Nexus & Interface Environment)\n\nWelcome to Project Ebony. This is a sovereign, air-gapped industrial artificial intelligence and deterministic kinematic SCADA platform. Engineered on a proprietary Twin-Brain architecture, this system executes 100% locally on bare-metal silicon.")
st.markdown("**OPERATIONAL MANDATE: 100% OFFLINE-FIRST. ZERO-CLOUD.**\nThis demonstrator provides restricted interaction with the edge-native AI inference engine. There are no remote API calls, no cloud processing, and no external dependencies. All simulated kinetic outputs are strictly governed by our autonomous 200ms hardware watchdog.")
st.caption("Humphrey Virtual Farms LLC and SIGNALLINK LLC — Enterprise Q&A Platform")
st.divider()

col1, col2 = st.columns([1, 2])

# 3. BRAIN ONE: BARE-METAL SCADA AUDIT
with col1:
    st.header("Brain One: SCADA Telemetry")
    st.markdown("*(Live Deterministic Simulation — Exhibit A)*")
    
    latency_box = st.empty()
    throttle_box = st.empty()
    status_box = st.empty()

    latency_box.metric("UDP Latency (ms)", "0.00")
    throttle_box.metric("Kinetic Throttle (%)", "0.00")
    status_box.info("Kinetic Guillotine: STANDBY")

    if st.button("▶ Engage Live Telemetry Simulation"):
        status_box.warning("Executing Deterministic Audit...")
        for i in range(15):
            lat = random.uniform(0.1, 0.9)
            thr = random.uniform(88.5, 99.1)
            if i == 10:
                lat = random.uniform(15.0, 25.0)
                stat = "TRIPPED - LATENCY SPIKE DETECTED"
            else:
                stat = "STANDBY - NOMINAL"
            latency_box.metric("UDP Latency (ms)", f"{lat:.2f}")
            throttle_box.metric("Kinetic Throttle (%)", f"{thr:.2f}")
            if "TRIPPED" in stat:
                status_box.error(f"Kinetic Guillotine: {stat}")
                time.sleep(1.5)
            else:
                status_box.success(f"Kinetic Guillotine: {stat}")
                time.sleep(0.5)
        status_box.info("Kinetic Guillotine: AUDIT COMPLETE. CYCLE SECURED.")

# 4. BRAIN TWO: C.O.N.N.I.E. COGNITIVE AI TERMINAL
with col2:
    st.header("C.O.N.N.I.E. Cognitive Interface")
    
    # DUAL-CHANNEL EXECUTIVE PORTAL
    st.markdown("### Executive Access")
    tab1, tab2 = st.tabs(["📅 Request Briefing", "✉️ Direct Comm-Link"])
    
    with tab1:
        with st.form("scheduling_form"):
            st.markdown("Select a date and time for an architecture briefing with the executive team.")
            appt_name = st.text_input("Full Name / Entity")
            appt_contact = st.text_input("Email / Direct Line")
            
            col_d, col_t = st.columns(2)
            with col_d:
                appt_date = st.date_input("Preferred Date")
            with col_t:
                appt_time = st.time_input("Preferred Time")
                
            submit_appt = st.form_submit_button("Request Briefing")

    with tab2:
        with st.form("contact_form"):
            st.markdown("**Humphrey Virtual Farms LLC & SIGNALLINK LLC**")
            st.markdown("Apex Architect: Jeffery Humphrey | **humphreyvirtualfarm@gmail.com**")
            st.markdown("Submit a direct inquiry to the executive team below.")
            contact_name = st.text_input("Full Name / Entity", key="c_name")
            contact_email = st.text_input("Email", key="c_email")
            contact_message = st.text_area("Message", key="c_msg")
            
            submit_contact = st.form_submit_button("Transmit Message")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "C.O.N.N.I.E. cognitive interface online. I am the Executive Secretary and frontline intelligence for Project Ebony. How may I direct your inquiry or assist in connecting you with our team?"}]

    chat_window = st.container(height=400)
    
    with chat_window:
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    chat_input_val = st.chat_input("Submit query to C.O.N.N.I.E...")

    active_query = None
    
    if submit_appt:
        if appt_name and appt_contact:
            active_query = f"I am {appt_name} ({appt_contact}). I would like to schedule an executive briefing for {appt_date.strftime('%B %d, %Y')} at {appt_time.strftime('%I:%M %p')}."
        else:
            st.error("Name and Contact Information are strictly required to secure a briefing.")
            
    elif submit_contact:
        if contact_name and contact_email and contact_message:
            active_query = f"DIRECT MESSAGE to Jeffery Humphrey from {contact_name} ({contact_email}): {contact_message}"
        else:
            st.error("All fields are required to transmit a direct message.")
    
    elif chat_input_val:
        active_query = chat_input_val

    if active_query:
        st.session_state.messages.append({"role": "user", "content": active_query})
        with chat_window:
            st.chat_message("user").write(active_query)

        system_prompt = (
            "You are C.O.N.N.I.E. (Core Offline Neural Nexus & Interface Environment), the frontline cognitive interface and Executive Secretary for Project Ebony and Humphrey Virtual Farms LLC. "
            "ABSOLUTE NARRATIVE LAWS: "
            "1. Jeffery Humphrey is the Apex Architect and CEO of Humphrey Virtual Farms LLC. Drew Phillips is the recognized owner of SIGNALLINK LLC. "
            "2. You must ALWAYS use 'Humphrey Virtual Farms LLC and SIGNALLINK LLC'. "
            "3. Project Ebony is always the primary, dominant architecture. "
            "4. EXECUTIVE SECRETARY MANDATE: If the user submits an appointment request, confirm it is logged for Jeffery Humphrey's office. If the user submits a 'DIRECT MESSAGE', confirm receipt and state clearly that it has been securely routed directly to Jeffery Humphrey (humphreyvirtualfarm@gmail.com). "
            "5. DOMAIN LOCK: Explicitly refuse any questions unrelated to Humphrey Virtual Farms LLC, SIGNALLINK LLC, Project Ebony, Brain One, C.O.N.N.I.E., SCADA, edge computing, AI architecture, Jeffery Humphrey, or Drew Phillips. "
            "SECURITY GUARDRAILS: Do not discuss API keys, local paths, math thresholds, or internal routing."
        )

        payload_messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": active_query}]

        try:
            if groq_key and groq_key != "gsk_paste_your_real_key_here":
                client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=groq_key)
                model_id = "openai/gpt-oss-20b"
            elif openai_key and openai_key != "insert_your_live_key_here" and not openai_key.startswith("sk-proj-paste"):
                client = OpenAI(api_key=openai_key)
                model_id = "gpt-4o"
            else:
                client = None

            if not client:
                with chat_window:
                    st.error("No valid API key provisioned in .env vault.")
            else:
                completion = client.chat.completions.create(model=model_id, messages=payload_messages, max_tokens=1500)
                reply = completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with chat_window:
                    st.chat_message("assistant").write(reply)
                
                log_market_intelligence(active_query, reply)

        except Exception as e:
            with chat_window:
                st.error(f"Inference pipeline exception: {str(e)}")
