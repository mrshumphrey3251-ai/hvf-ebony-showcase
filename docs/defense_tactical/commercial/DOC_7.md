# ℹ️ DOC 7: COMMAND FAQ
**Document ID:** HDT-COM-DOC-007

## 1. FREQUENTLY ASKED QUESTIONS
* **Q: Who holds the cryptographic keys?** 
  * A: The local commander. HDT has zero backdoor access.
* **Q: What happens if the Master Node loses power?** 
  * A: The SQLite WAL vault guarantees data integrity up to the millisecond of power loss. Upon reboot, operations resume instantly.