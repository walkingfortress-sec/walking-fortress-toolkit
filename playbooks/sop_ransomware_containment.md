# SOP-01: Ransomware Containment & Recovery Playbook

| Phase | Operational Steps | Target Telemetry / Tools |
|---|---|---|
| **1. Identification** | Detect mass file modification, shadow copy deletion (`vssadmin delete shadows`), or `bcdedit` boot status alteration. | Sysmon Event ID 1 (`vssadmin.exe`, `wbadmin.exe`), Windows Event ID 4688 |
| **2. Containment** | Disconnect host interface via SOAR daemon or netsh firewall block rule. Isolate infected subnet immediately. | `soar/auto_responder_daemon.py`, Active Directory GPO Isolation |
| **3. Eradication** | Identify ransomware binary parent process via Process Explorer/Sysmon log tree; terminate malicious execution threads. | Sysmon Event ID 1 & Event ID 5 (Process Terminated) |
| **4. Recovery** | Restore encrypted shares from immutable offline backups; rebuild endpoint operating system image; verify clean baseline. | Backup Verification Engine, Windows PE Deployment |
| **5. Post-Incident** | Ingest IOC file hashes and C2 IPs into SIEM blocklists; document timeline and root cause. | Splunk Threat Intelligence Lookup Tables |