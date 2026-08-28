# Enterprise Windows Host Hardening Baseline Standard

## 1. PowerShell Auditing Policies
* **Script Block Logging (Event ID 4104):** Enabled for all code execution blocks.
* **Module Logging (Event ID 4103):** Pipeline execution detail enabled for core modules (`*`).
* **Transcription Logging:** Enabled; written to isolated centralized directory.

## 2. Windows Event Log Policies
* **Command Line Process Auditing (Event ID 4688):** Enabled with "Include command line in process creation events".
* **Kerberos Auditing:** Audit Kerberos Service Ticket Operations enabled (Success & Failure) for TGS tracking.

## 3. Privilege & Credential Safeguards
* **LAPS Integration:** Local Administrator Password Solution deployed; unique passwords auto-rotated every 30 days.
* **Credential Guard:** Virtualization-based security enabled to isolate LSASS process memory.