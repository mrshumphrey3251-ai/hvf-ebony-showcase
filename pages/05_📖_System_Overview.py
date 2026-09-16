import streamlit as st

st.markdown("# 📖 System Overview & Commercial Suite")
st.info("Publicly viewable commercial tiers and platform documentation.")

col_p1, col_p2, col_p3, col_p4 = st.columns(4)
with col_p1:
    st.markdown("### 🌱 PERSONAL")
    st.markdown("**$19.99/mo**\n* Single-User Node\n* Dual-Engine AI")
    st.button("Subscribe Personal", use_container_width=True)
with col_p2:
    st.markdown("### 💎 VIP MEMBER")
    st.markdown("**$249/mo**\n* Drone Spectator\n* GLI Analytics")
    st.button("Subscribe VIP", use_container_width=True)
with col_p3:
    st.markdown("### 🏛️ ENTERPRISE")
    st.markdown("**$2,499/yr**\n* Client Dashboard\n* Issue Staff Keys")
    st.button("Subscribe Enterprise", use_container_width=True)
with col_p4:
    st.markdown("### 📦 HARDWARE")
    st.markdown("**$4,950 setup**\n* Physical Server\n* 100% Air-Gapped")
    st.button("Order Hardware", use_container_width=True)

st.divider()
st.subheader("Sovereign Knowledge Academy")
with st.expander("🏛️ [PILLAR 1]: The Humphrey Virtual Farm Manifesto"):
    st.write("Engineered by Founder & CEO Jeffery Humphrey. 100% Air-Gapped Compute. Absolute Data Ownership.")
with st.expander("⚡ [PILLAR 2]: Ebony - Neural Processing & Predictive Memory"):
    st.write("Dual-engine agronomic intelligence. Cloud Fast Link (Groq) & Sovereign Local Core (Ollama).")
