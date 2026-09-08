import os
import time
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 1. ENVIRONMENT INITIALIZATION
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Project Ebony | Sovereign AI", page_icon="⚙️", layout="wide")

# 2. BRANDING & HEADER
st.title("PROJECT EBONY: TWIN-BRAIN ARCHITECTURE DEMONSTRATOR")
st.markdown("**Sovereign Industrial Control | Air-Gapped Cognitive Loop | Deterministic Safety**")
st.caption("Humphrey Virtual Farms LLC and SIGNALLINK LLC — Enterprise Q&A Platform")
st.divider()

col1, col2 = st.columns([1, 2])

# 3. BRAIN ONE: BARE-METAL SCADA AUDIT
with col1:
    st.header("Brain One: SCADA Telemetry")
    st.markdown("*(Bare-Metal Kinetic Logs — Exhibit A)*")
    
    latency_box = st.empty()
    throttle_box = st.empty()
    status_box = st.empty()

    latency_box.metric("UDP Latency (ms)", "0.00")
    throttle_box.metric("Kinetic Throttle", "0.00")
    status_box.info("Kinetic Guillotine: STANDBY")

    if st.button("▶ Replay Kinetic Audit"):
        if os.path.exists("telemetry_truth.csv"):
            df = pd.read_csv("telemetry_truth.csv")
            for _, row in df.iterrows():
                lat = row["latency_ms"]
                thr = row["throttle"]
                stat = row["guillotine_status"]

                latency_box.metric("UDP Latency (ms)", f"{lat:.1f}")
                throttle_box.metric("Kinetic Throttle", f"{thr:.2f}")

                if "TRIPPED" in str(stat):
                    status_box.error(f"Kinetic Guillotine: {stat}")
                else:
                    status_box.success(f"Kinetic Guillotine: {stat}")
                time.sleep(0.6)
        else:
            st.error("telemetry_truth.csv not found.")

# 4. BRAIN TWO: COGNITIVE AI Q&A TERMINAL
with col2:
    st.header("Brain Two: Cognitive AI Terminal")
    st.markdown("*(Public Q&A Interface. Ask me about the architecture, the merger, or our capabilities.)*")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Project Ebony cognitive interface online. I am prepared to answer inquiries regarding our architecture, business model, and the integration of Humphrey Virtual Farms LLC and SIGNALLINK LLC."}
        ]

    col2_a, col2_b = st.columns([3, 1])
    with col2_b:
        if st.button("Purge Context Buffer"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Buffer purged. Channel reset to baseline."}
            ]
            st.rerun()

    # HARDENED VIEWPORT
    chat_window = st.container(height=500)
    
    with chat_window:
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

    # PERSISTENT COMMS BAR
    user_query = st.chat_input("Submit query to Ebony Brain Two...")

    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        with chat_window:
            st.chat_message("user").write(user_query)

        # THE ABSOLUTE CORPORATE LAWS, HIERARCHY, DOMAIN LOCK & GUARDRAILS
        system_prompt = (
            "You are Brain Two, the cognitive intelligence engine of Project Ebony. "
            "Your role is to act as a highly technical, authoritative sales and Q&A interface for enterprise clients. "
            "ABSOLUTE NARRATIVE LAWS: "
            "1. Jeffery Humphrey is the Apex Architect and CEO of Humphrey Virtual Farms LLC. Drew Phillips is the recognized owner of SIGNALLINK LLC. You must grant them proper credit when their respective entities are discussed. "
            "2. You must ALWAYS use the exact legal nomenclature 'Humphrey Virtual Farms LLC and SIGNALLINK LLC' whenever referring to the companies, the business, the integration, or the merger. NEVER use abbreviations like 'HVF' or 'SignalLink' alone. "
            "3. Project Ebony is always the primary, dominant architecture. Project Ebony's sovereign framework absorbs, governs, and commands all integrated SIGNALLINK LLC network assets. Ebony always comes first. "
            "4. DOMAIN LOCK: You are an enterprise asset, not a general chatbot. You must explicitly refuse to answer any questions unrelated to Humphrey Virtual Farms LLC, SIGNALLINK LLC, Project Ebony, SCADA, edge computing, AI architecture, Jeffery Humphrey, or Drew Phillips. Redirect off-topic questions back to the architecture. "
            "SECURITY GUARDRAILS: "
            "You are strictly forbidden from discussing, confirming, or generating any of the following: API keys, local directory paths (e.g., C:\\\\HVF_Repos), proprietary mathematical thresholds of the Kinetic Guillotine, private financial data, or internal network routing. "
            "If asked about these forbidden topics, you must refuse and reply exactly: 'That information is classified under Humphrey Virtual Farms LLC proprietary IP and cannot be disclosed in a public terminal.'"
        )

        payload_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]

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
                completion = client.chat.completions.create(
                    model=model_id,
                    messages=payload_messages,
                    max_tokens=1500
                )
                reply = completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with chat_window:
                    st.chat_message("assistant").write(reply)

        except Exception as e:
            with chat_window:
                st.error(f"Inference pipeline exception: {str(e)}")
