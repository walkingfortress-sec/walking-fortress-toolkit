# Threat Hunting Playbook: Lateral Movement Detection

| Technique | MITRE ID | Target Telemetry | Detection Logic / SPL |
|---|---|---|---|
| **WMI Remote Execution** | T1047 | Sysmon Event ID 1 / Event ID 19 | `index=win_telemetry EventCode=1 Image="*\\wmic.exe" CommandLine="*/node:*" OR ParentImage="*\\wmiprvse.exe"` |
| **PsExec Service Creation** | T1021.002 | Windows Security Event 7045 | `index=win_telemetry EventCode=7045 ServiceName="PSEXESVC" OR ServiceFileName="*\\PSEXESVC.exe"` |
| **WinRM Remote Management** | T1021.006 | Windows Security Event 4624 (Logon Type 10 / 3) | `index=win_telemetry EventCode=4624 LogonType=3 ProcessName="*\\wsmprovhost.exe"` |

## Triage Protocol
1. **Logon Correlation:** Map source IP from Event 4624 against corporate network assets to isolate jump hosts.
2. **Process Lineage:** Trace child processes spawned by `wmiprvse.exe` or `wsmprovhost.exe` for unauthorized PowerShell or CMD execution.
3. **Containment Trigger:** Pass source host IP to `soar/auto_responder_daemon.py` if lateral movement execution is confirmed.