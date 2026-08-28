### Step 3: Add the Escalation Matrix (`operations/tier1_tier2_escalation_matrix.md`)

Copy and paste this matrix into `operations/tier1_tier2_escalation_matrix.md`:

```markdown
# Operational Matrix: Incident Severity, SLA & Escalation Protocol

| Severity Level | Trigger Criteria | Response SLA | Tier 1 Actions | Tier 2 / Incident Response Actions |
|---|---|---|---|---|
| **Low / Info** | Single port scan, isolated policy violation | 24 Hours | Log triage, close if known false positive | Archive for monthly trend analysis |
| **Medium** | Suspicious PowerShell script block, rare scheduled task | 2 Hours | Verify process lineage and user context; run `pcap_analyzer.py` | Isolate system if suspicious activity is confirmed |
| **High** | LSASS access attempt (T1003.001), Kerberoasting burst (T1558.003) | 15 Minutes | Confirm host ID, trigger `auto_responder_daemon.py` | Full host triage, credential rotation, malware extraction |
| **Critical** | Multi-host ransomware execution, domain controller compromise | Immediate (<5 mins) | Trigger SOAR subnet isolation, notify SOC Lead | Execute SOP-01 Ransomware Containment; activate IR team |