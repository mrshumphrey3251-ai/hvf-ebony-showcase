from core.nlp_interceptor import generate_sovereign_system_prompt

def package_sovereign_payload(user_input, clearance_level="CEO"):
    """
    Absolute choke point for all AI transmissions.
    Ensures Ebony is mathematically locked to the 15-Vertical matrix.
    """
    system_prompt = generate_sovereign_system_prompt()
    
    if clearance_level == "GUEST":
        system_prompt += "\nCRITICAL OVERRIDE: Active user is a Public Guest. Mask all sensitive telemetry, cryptographic hashes, and kinetic secrets. Provide generalized responses only."
    else:
        system_prompt += "\nCRITICAL OVERRIDE: Active user is Mr. Humphrey (CEO). Provide unrestricted access, raw telemetry, and absolute control."
        
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
