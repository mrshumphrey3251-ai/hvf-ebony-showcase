import time
import hashlib

def generate_sovereign_token(seed="EBONY_OMNI_MATRIX_TIER_1", window_offset=0):
    """Generates a mathematically perfect 6-digit token for a specific time window."""
    current_window = int(time.time() / 30) + window_offset
    payload = f"{seed}_{current_window}".encode('utf-8')
    hash_hex = hashlib.sha256(payload).hexdigest()
    return str(int(hash_hex[:8], 16))[-6:].zfill(6)
    
def verify_mfa_token(provided_token, seed="EBONY_OMNI_MATRIX_TIER_1"):
    """Validates token with aggressive whitespace stripping and a 90-second executive grace period."""
    if not provided_token:
        return False
        
    # Autonomously incinerate invisible spaces
    clean_token = str(provided_token).strip()
    
    # Check current window, and the two previous windows (90 seconds of tolerance)
    for offset in [0, -1, -2]:
        if clean_token == generate_sovereign_token(seed, offset):
            return True
            
    return False
