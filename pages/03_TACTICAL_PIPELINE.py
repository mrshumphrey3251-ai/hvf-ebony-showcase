import streamlit as st
import sys
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

st.set_page_config(page_title="EBONY // TACTICAL PIPELINE", layout="wide", initial_sidebar_state="expanded")

if "active_identity" not in st.session_state:
    st.error("ACCESS DENIED. IDENTITY VERIFICATION REQUIRED AT ROOT.")
    st.stop()

st.markdown("# 🎯 TACTICAL PIPELINE INGESTION")
st.caption("GOVERNMENT, DEFENSE & COMMERCIAL TARGET MATRIX // CEO EYES ONLY")
st.divider()

st.success(f"**ACTIVE CLEARANCE:** {st.session_state.active_identity} - AUTHORIZED TO DICTATE ENGAGEMENT.")

# --- PERSISTENT LEDGER FOR TARGETS ---
ledger_path = os.path.join(parent_dir, "core", "target_ledger.json")

if not os.path.exists(ledger_path):
    with open(ledger_path, "w") as f:
        json.dump([], f)

def load_targets():
    with open(ledger_path, "r") as f:
        return json.load(f)

def save_targets(data):
    with open(ledger_path, "w") as f:
        json.dump(data, f, indent=4)

if "targets" not in st.session_state:
    st.session_state.targets = load_targets()

st.subheader("PIPELINE INGESTION BAY")
st.write("Awaiting Tier-2 intelligence payload. Paste the target data below to generate the executive directive matrix.")

raw_checklist = st.text_area("Paste SignalLink Target Payload:", height=150)

if st.button("INGEST TARGET", type="primary", use_container_width=True):
    if raw_checklist:
        new_target = {
            "id": len(st.session_state.targets) + 1,
            "raw_text": raw_checklist,
            "decisions": {
                "Interested": False,
                "Not Interested": False,
                "Join the Call": False,
                "You Take Lead": False,
                "Ebony/HVF Should Be Presented": False,
                "SignalLink Only": False,
                "Joint Outreach": False,
                "Needs More Review": False
            }
        }
        st.session_state.targets.append(new_target)
        save_targets(st.session_state.targets)
        st.success("PIPELINE INGESTED. Target secured in the Omni-Matrix ledger.")
        st.rerun()
    else:
        st.warning("AWAITING CHECKLIST PAYLOAD.")

st.divider()
st.subheader("EXECUTIVE DIRECTIVES")

if not st.session_state.targets:
    st.info("Matrix is empty. Standing by for incoming transmission from Drew.")
else:
    for idx, target in enumerate(st.session_state.targets):
        with st.expander(f"TARGET ACQUISITION #{target['id']} // AWAITING CEO OVERRIDE", expanded=True):
            st.text("INTELLIGENCE PAYLOAD:")
            st.info(target["raw_text"])
            
            st.markdown("**DICTATE TERMS OF ENGAGEMENT:**")
            cols = st.columns(4)
            decisions = target["decisions"]
            
            decisions["Interested"] = cols[0].checkbox("Interested", value=decisions["Interested"], key=f"int_{idx}")
            decisions["Not Interested"] = cols[0].checkbox("Not Interested", value=decisions["Not Interested"], key=f"n_int_{idx}")
            
            decisions["Join the Call"] = cols[1].checkbox("Join the Call", value=decisions["Join the Call"], key=f"join_{idx}")
            decisions["You Take Lead"] = cols[1].checkbox("You Take Lead", value=decisions["You Take Lead"], key=f"lead_{idx}")
            
            decisions["Ebony/HVF Should Be Presented"] = cols[2].checkbox("Ebony/HVF Should Be Presented", value=decisions["Ebony/HVF Should Be Presented"], key=f"eb_{idx}")
            decisions["SignalLink Only"] = cols[2].checkbox("SignalLink Only", value=decisions["SignalLink Only"], key=f"sig_{idx}")
            
            decisions["Joint Outreach"] = cols[3].checkbox("Joint Outreach", value=decisions["Joint Outreach"], key=f"joint_{idx}")
            decisions["Needs More Review"] = cols[3].checkbox("Needs More Review", value=decisions["Needs More Review"], key=f"rev_{idx}")

            if st.button("LOCK IN DIRECTIVE", key=f"save_{idx}", type="secondary"):
                target["decisions"] = decisions
                save_targets(st.session_state.targets)
                st.success(f"DIRECTIVE LOCKED. Target #{target['id']} updated in the master ledger.")
