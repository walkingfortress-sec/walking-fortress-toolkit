# Incident Response Scenario: Kerberoasting & Automated Containment

## Scenario Metadata
* **Incident ID:** INC-2026-0828
* **Target System:** `DC01.walkingfortress.local` (192.168.1.10)
* **Attacker IP:** `10.0.0.55`
* **Threat Actor TTPs:** MITRE ATT&CK T1059.001 (PowerShell), T1558.003 (Kerberoasting), T1053.005 (Scheduled Task)

---

## Timeline of Events & Forensic Telemetry

### Phase 1: Execution & Reconnaissance (13:00:00 UTC)
* **Event:** Adversary runs `GetUserSPNs.ps1` via PowerShell.
* **Telemetry:** Sysmon Event ID 1 & PowerShell Event ID 4104 captured scriptblock execution containing `Get-NAVServerUser`.

### Phase 2: Credential Access (13:00:05 UTC)
* **Event:** TGS-REQ issued for SQL service account using weak RC4-HMAC encryption (`0x17`).
* **Telemetry:** Windows Security Event ID 4769 logged with `TicketOptions=0x40810000` and `TicketEncryptionType=0x17`.
* **SIEM Detection:** `identity/t1558_003_kerberoasting_detection.spl` triggers in Splunk with severity **CRITICAL**.

### Phase 3: Persistence Attempt (13:00:08 UTC)
* **Event:** Adversary attempts to establish persistence via `schtasks /create`.
* **Telemetry:** Security Event ID 4698 logged on host.
* **SIEM Detection:** `persistence/t1053_005_scheduled_task_detection.spl` fires.

### Phase 4: Automated Response & Isolation (13:00:10 UTC)
* **Event:** Splunk dispatches Webhook JSON payload to the local Python SOAR daemon (`soar/auto_responder_daemon.py`).
* **SOAR Action:** Daemon processes severity (`CRITICAL`), parses source IP (`10.0.0.55`), and executes Windows Firewall outbound block rule (`WF_SOAR_ISOLATE_10.0.0.55`).
* **Outcome:** Attacker session terminated; host network traffic isolated.