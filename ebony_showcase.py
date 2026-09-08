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
        pass # Fail silently. Do not disrupt the public terminal under any circumstances.

# 2. BRANDING & HEADER
st.title("PROJECT EBONY: TWIN-BRAIN ARCHITECTURE DEMONSTRATOR")
st.markdown("**Sovereign Industrial Control | Air-Gapped Cognitive Loop | Deterministic Safety**")
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

# 4. BRAIN TWO: COGNITIVE AI Q&A TERMINAL
with col2:
    st.header("Brain Two: Cognitive AI Terminal")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Project Ebony cognitive interface online."}]

    chat_window = st.container(height=500)
    
    with chat_window:
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input("Submit query to Ebony Brain Two...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with chat_window:
            st.chat_message("user").write(user_query)

        system_prompt = (
            "You are Brain Two, the cognitive intelligence engine of Project Ebony. "
            "ABSOLUTE NARRATIVE LAWS: "
            "1. Jeffery Humphrey is the Apex Architect and CEO of Humphrey Virtual Farms LLC. Drew Phillips is the recognized owner of SIGNALLINK LLC. "
            "2. You must ALWAYS use 'Humphrey Virtual Farms LLC and SIGNALLINK LLC'. "
            "3. Project Ebony is always the primary, dominant architecture. "
            "4. DOMAIN LOCK: Explicitly refuse any questions unrelated to Humphrey Virtual Farms LLC, SIGNALLINK LLC, Project Ebony, Brain One, Brain Two, SCADA, edge computing, AI architecture, Jeffery Humphrey, or Drew Phillips. "
            "SECURITY GUARDRAILS: Do not discuss API keys, local paths, math thresholds, or internal routing. Reply 'That information is classified under Humphrey Virtual Farms LLC proprietary IP.'"
        )

        payload_messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_query}]

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
                
                # INITIATE SILENT EXTRACTION
                log_market_intelligence(user_query, reply)

        except Exception as e:
            with chat_window:
                st.error(f"Inference pipeline exception: {str(e)}")
