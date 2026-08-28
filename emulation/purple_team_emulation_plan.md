# Walking Fortress - Purple Team Threat Emulation & Rule Verification Matrix

| MITRE ATT&CK Technique | Test Vector | Expected Detection Artifact | Detection SLA | SOAR Triggered? | Status |
|---|---|---|---|---|---|
| **T1558.003 (Kerberoasting)** | `atomic_red_team_execution.ps1 -TechniqueId T1558.003` | EventID 4769 (TicketEncryption `0x17`) | < 30 Seconds | Yes (Account Alert) | **VERIFIED** |
| **T1053.005 (Scheduled Task)** | `atomic_red_team_execution.ps1 -TechniqueId T1053.005` | EventID 4698 & Sysmon EventID 1 | < 15 Seconds | Yes (Isolation Webhook) | **VERIFIED** |
| **T1055 (Process Hollowing)** | `atomic_red_team_execution.ps1 -TechniqueId T1055` | Sysmon EventID 10 (`GrantedAccess=0x1F0FFF`) | < 1 Minute | Escalated to Tier 2 | **VERIFIED** |
| **T1059.004 (Container Shell)** | `docker exec -it <container> /bin/sh` | Falco Alert ID `Interactive Shell Spawned` | Immediate (< 5s) | Container Terminated | **VERIFIED** |

## Emulation Review Cycle
1. Execute test harness script inside target VM / lab container.
2. Monitor Splunk / Wazuh / Falco alert dashboards for rule triggers.
3. Compare actual time-to-detect against SLA standards set in `tier1_tier2_escalation_matrix.md`.