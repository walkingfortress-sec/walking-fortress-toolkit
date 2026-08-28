# Walking Fortress: Purple Team Detection Validation Matrix

| MITRE ATT&CK ID | Technique Name | Simulation Method | Expected Host Telemetry | Expected SIEM Alert Rule | Status |
|---|---|---|---|---|---|
| **T1003.001** | Credential Dumping: LSASS | `rundll32 comsvcs.dll, MiniDump` | Sysmon EventID 10 (Target: `lsass.exe`) | `Walking Fortress - LSASS Process Access` | Validated |
| **T1059.001** | Execution: PowerShell | `powershell -EncodedCommand` | Sysmon EventID 1 / Event 4104 | `Walking Fortress - Obfuscated PowerShell` | Validated |
| **T1136.001** | Persistence: Local Account | `net user /add` | Windows EventID 4720 | `Walking Fortress - Rogue Account Creation` | Validated |

## Validation Protocol
1. **Red Stage:** Run simulation script from `simulations/` on target lab workstation.
2. **Blue Stage:** Check Splunk index `win_telemetry` for corresponding EventCode within 60 seconds.
3. **Verification:** Confirm rule severity fires correctly and dispatches trigger payload.