import re

def parse_kinetic_intent(user_input):
    """
    SEMANTIC KINETIC PARSER
    Translates executive voice commands into physical hardware parameters.
    """
    input_lower = user_input.lower()
    
    # 1. Detect Vertical 15 / Warehousing -> Hypoxic Vent
    if "vertical 15" in input_lower or "warehousing" in input_lower:
        if "hypoxic vent" in input_lower or "vent" in input_lower:
            return {
                "intent_detected": True,
                "vertical": "📦 WAREHOUSING",
                "target_node": "TARGET ALL NODES",
                "pwr_state": True,
                "actuator_state": True,
                "kinetic_rate": 100,
                "action_desc": "HYPOXIC VENT EXECUTED. NITROGEN FLOOD ACTIVE."
            }
            
    # 2. Detect Vertical 11 / Mining -> TBM Thrust
    if "vertical 11" in input_lower or "mining" in input_lower:
        if "thrust" in input_lower or "advance" in input_lower:
            return {
                "intent_detected": True,
                "vertical": "⛏️ MINING",
                "target_node": "TBM-OMEGA-01",
                "pwr_state": True,
                "actuator_state": True,
                "kinetic_rate": 85,
                "action_desc": "TBM THRUST ENGAGED. ADVANCING AT 85% RPM."
            }

    # No kinetic intent found, return to standard NLP response
    return {"intent_detected": False}
