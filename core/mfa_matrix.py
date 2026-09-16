import time
import hashlib

def generate_sovereign_token(seed="EBONY_OMNI_MATRIX_TIER_1"):
    """Generates a mathematically perfect 6-digit token that self-destructs every 30 seconds."""
    current_window = int(time.time() / 30)
    payload = f"{seed}_{current_window}".encode('utf-8')
    hash_hex = hashlib.sha256(payload).hexdigest()
    return str(int(hash_hex[:8], 16))[-6:].zfill(6)
    
def verify_mfa_token(provided_token, seed="EBONY_OMNI_MATRIX_TIER_1"):
    """Validates token and allows a 1-window grace period for network drift."""
    valid_token = generate_sovereign_token(seed)
    
    prev_window = int(time.time() / 30) - 1
    prev_payload = f"{seed}_{prev_window}".encode('utf-8')
    prev_hash_hex = hashlib.sha256(prev_payload).hexdigest()
    prev_token = str(int(prev_hash_hex[:8], 16))[-6:].zfill(6)
    
    return provided_token == valid_token or provided_token == prev_token
