# Walking Fortress IR-SOP-402: Correlated Host & Network Telemetry Triage

## 1. Alert Overview
* **Playbook ID:** WF-IRP-402
* **Severity:** HIGH
* **Primary Vectors:** MITRE ATT&CK T1059.001 (PowerShell), T1071.001 (Web Protocols)
* **Telemetry Sources:** Windows Sysmon (Events 1, 3, 13), Event 4104, Zeek (`conn.log`, `dns.log`, `http.log`)

## 2. Triage Workflow

### Phase 1: Initial Telemetry Verification
1. **Query Verification:** Run `host_network_correlation.spl` in Splunk to confirm the joint trigger.
2. **Anchor Extraction:** Extract `SourceAddress / id_orig_h`, `DestinationAddress / id_resp_h`, `DestinationPort`, `Image`, and `CommandLine`.
3. **Time Window Check:** Confirm endpoint process initiation and network connection setup occurred within a 5-second delta.

### Phase 2: Endpoint Context Enrichment
* **Parent Process Analysis:** Check Sysmon Event 1 for anomalous parent binaries (e.g., `wmiprvse.exe`, `excel.exe`).
* **Deobfuscation:** Inspect PowerShell Event 4104 logs for base64 encoded strings or `Net.WebClient` download cradles.

### Phase 3: Network Layer Deep Dive
* **DNS Resolution:** Inspect `zeek:dns` log for oversized queries or high-entropy dynamic subdomains.
* **HTTP/SSL Inspection:** Review `zeek:http` and `zeek:ssl` for unrated User-Agents or untrusted TLS certificates.

## 3. Containment & Remediation
1. **Host Isolation:** Isolate host from network via EDR / local host firewall.
2. **Network Blocking:** Push destination IP/domain to edge perimeter blocklists.
3. **Account Reset:** Revoke active Kerberos tickets and reset passwords for impacted domain accounts.