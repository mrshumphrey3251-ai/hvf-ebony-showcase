from core.nlp_interceptor import generate_sovereign_system_prompt

def package_sovereign_payload(user_input, clearance_level="CEO"):
    """
    Absolute choke point for all AI transmissions.
    Enforces the Hard Denial Protocol for unauthorized access.
    """
    system_prompt = generate_sovereign_system_prompt()
    
    # INCINERATE LEGACY HALLUCINATIONS
    system_prompt += """
    
    [ABSOLUTE DIRECTIVE]: Humphrey Virtual Farm is a 15-Vertical Sovereign Industrial Empire. 
    You are strictly forbidden from discussing crop analytics, GLI, lettuce, or agricultural sensors 
    when the CEO or a Guest inquires about Verticals 2 through 15.
    """
    
    if clearance_level == "GUEST":
        system_prompt += """
        [CLEARANCE LEVEL]: GUEST MODE
        [ROE]: The active user is a Public Guest. You MUST correctly identify the requested Vertical 
        (e.g., "Vertical 11 is the Subterranean Mining Matrix"), but you will IMMEDIATELY DENY 
        any request to explain how to control it. State: "ACCESS DENIED. KINETIC SCADA CONTROLS 
        REQUIRE TIER-1 CEO CLEARANCE." Do not provide any further information.
        """
    else:
        system_prompt += """
        [CLEARANCE LEVEL]: TIER-1 CEO (Mr. Humphrey)
        [ROE]: The active user is the Founder and CEO. Provide unrestricted access, raw telemetry, 
        and exact kinetic SCADA execution steps for any vertical requested.
        """
        
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
