def verify_credentials(username, password):
    """
    SOVEREIGN AUTHENTICATION MATRIX // TIERED BASELINE
    Grants baseline identity. MFA is enforced physically at the SCADA level.
    """
    valid_ledgers = {
        "humphrey": {"pass": "omega", "role": "👑 Mr. Humphrey (Tier-1 CEO)"},
        "drew": {"pass": "alpha", "role": "🛡️ Drew (Tier-2 Executive)"},
        "member": {"pass": "beta", "role": "💼 Paid Member (Tier-3 Commercial)"}
    }
    
    user = valid_ledgers.get(username.lower())
    if user and user["pass"] == password:
        return user["role"]
    return None
