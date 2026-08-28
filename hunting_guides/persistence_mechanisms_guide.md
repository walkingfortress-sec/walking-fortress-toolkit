# Threat Hunting Playbook: Advanced Persistence Mechanisms

| Persistence Vector | Target Telemetry | Splunk / Wazuh Rule Focus |
|---|---|---|
| **New Service Installation** | Windows Event ID 7045 / Sysmon Event ID 1 | `index=win_telemetry EventCode=7045 | stats count by ServiceName ServiceFileName host` |
| **Accessibility Features Hijack** | Sysmon Event ID 1 (`sethc.exe`, `utilman.exe`) | Match parent process executions where `cmd.exe` or `powershell.exe` replaces binary targets. |
| **Registry Run Key Modification** | Sysmon Event ID 12 / 13 / 14 | Track modifications to `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run*`. |

## Investigation Steps
1. Filter out known administrative software updates via clean baseline lookup tables.
2. Check binary signature status on all newly registered services using Sysmon Event ID 7 (Image Loaded).
3. Validate persistence persistence artifacts against MITRE ATT&CK T1546 / T1543 tags.