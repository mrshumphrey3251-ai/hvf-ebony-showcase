# ℹ️ DOC 7: COMMAND FAQ
**Document ID:** HDT-COM-DOC-007

## 1. FREQUENTLY ASKED QUESTIONS
* **Q: Who holds the cryptographic keys?** 
  * **A:** The local commander. HDT has zero backdoor access. No corporate entity can override a FOB.
* **Q: What happens if the Master Node loses power during an engagement?** 
  * **A:** The SQLite WAL vault guarantees data integrity up to the exact millisecond of power loss. Upon reboot, operations and memory resume instantly without corruption.
* **Q: Can the drones operate if the Tailscale mesh goes down?**
  * **A:** Yes. Assets fall back to local RF controller logic and autonomous RTB (Return to Base) protocols.