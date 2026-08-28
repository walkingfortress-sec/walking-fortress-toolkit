# SOP-02: Data Exfiltration & Insider Threat Triage Playbook

| Phase | Action Steps | Telemetry & Artifacts |
|---|---|---|
| **1. Ingestion** | Monitor high-volume outbound network traffic to rare external IPs or cloud storage endpoints (Mega, Dropbox). | Zeek `conn.log` / `http.log`, Suricata EVE alert |
| **2. Staging Inspection** | Check local endpoint temporary directories for archive file creation (`.zip`, `.rar`, `.7z`) over 500MB. | Sysmon Event ID 11 (FileCreate in `%TEMP%` or `C:\Users\Public\`) |
| **3. USB & Egress Triage** | Inspect USB storage insertion events and external drive mounting logs. | Windows Event ID 20001 / Event ID 20002 (Driver Frameworks) |
| **4. Mitigating Response** | Terminate staging processes, revoke user Active Directory active token sessions, and issue egress block rule on proxy. | PowerShell `Revoke-AzureADUserAllRefreshToken` / Firewall Drop |