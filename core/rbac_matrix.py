def evaluate_clearance(user_tier, action_type="READ"):
    """
    SOVEREIGN RBAC MATRIX
    Invisible cryptographic doors dictating access based on clearance tier.
    Tiers: 1 (CEO), 2 (Drew), 3 (Member), 4 (Guest)
    """
    
    # Tier-1 (CEO): Absolute Omni-Matrix Authority
    if user_tier == 1:
        return {"access_granted": True, "msg": "TIER-1 CEO CLEARANCE ACCEPTED. OMNI-MATRIX UNLOCKED."}
        
    # Tier-2 (Drew / Executive): Standard Actuation, No Lethal/Emergency Overrides
    if user_tier == 2:
        if action_type in ["LETHAL", "ZERO_DAY", "EMERGENCY_OVERRIDE"]:
            return {"access_granted": False, "msg": "ACCESS DENIED. ACTION CLASSIFIED AS TIER-1 EXECUTIVE OVERRIDE. DREW/EXECUTIVE CLEARANCE INSUFFICIENT."}
        return {"access_granted": True, "msg": "TIER-2 EXECUTIVE CLEARANCE ACCEPTED. STANDARD SCADA UNLOCKED."}
        
    # Tier-3 (Paid Member): Read-Only Telemetry, Zero Kinetic Actuation
    if user_tier == 3:
        if action_type in ["KINETIC", "LETHAL", "ZERO_DAY", "EMERGENCY_OVERRIDE"]:
            return {"access_granted": False, "msg": "ACCESS DENIED. COMMERCIAL MEMBERSHIP PERMITS READ-ONLY TELEMETRY. SCADA ACTUATION LOCKED."}
        return {"access_granted": True, "msg": "TIER-3 MEMBER CLEARANCE ACCEPTED. TELEMETRY STREAM ONLINE."}
        
    # Tier-4 (Guest): Absolute Lockout
    return {"access_granted": False, "msg": "ACCESS DENIED. GUEST CLEARANCE INSUFFICIENT FOR SOVEREIGN OPERATIONS."}

def map_identity_to_tier(identity_string):
    """Maps the UI identity selection to the mathematical tier."""
    if "CEO" in identity_string: return 1
    if "Drew" in identity_string: return 2
    if "Member" in identity_string: return 3
    return 4
