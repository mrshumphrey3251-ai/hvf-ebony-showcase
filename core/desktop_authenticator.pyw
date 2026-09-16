import sys
import os
import time
import tkinter as tk

# Ensure strict pathing to the core matrix
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from mfa_matrix import generate_sovereign_token

def update_token():
    """Autonomously refreshes the cryptographic hash every 1000ms."""
    lbl_token.config(text=generate_sovereign_token())
    root.after(1000, update_token)

# Build the Sovereign HUD
root = tk.Tk()
root.title("EBONY MFA")
root.geometry("300x120")
root.attributes("-topmost", True) # Locks the window on top of all other applications
root.configure(bg="#0E1117")

tk.Label(root, text="TIER-1 SOVEREIGN TOKEN", fg="#00FFAA", bg="#0E1117", font=("Consolas", 12, "bold")).pack(pady=10)
lbl_token = tk.Label(root, text="------", fg="#FFFFFF", bg="#0E1117", font=("Consolas", 32, "bold"))
lbl_token.pack()

update_token()
root.mainloop()
