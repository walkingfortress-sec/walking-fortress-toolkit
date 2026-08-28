# Sysmon Configuration & MITRE ATT&CK Mapping Baseline

| Sysmon Event ID | Event Type | Primary MITRE ATT&CK Mapping | Security Focus |
|---|---|---|---|
| **Event ID 1** | Process Creation | T1059 (Command & Scripting Interpreter) | Full command line auditing, parent process lineage |
| **Event ID 3** | Network Connection | T1071 (Application Layer Protocol) | Egress connections, C2 beaconing |
| **Event ID 7** | Image Loaded | T1574 (Hijack Execution Flow) | Unsigned DLL side-loading detection |
| **Event ID 8** | CreateRemoteThread | T1055 (Process Injection) | Process hollowing and injection triage |
| **Event ID 11** | FileCreate | T1105 (Ingress Tool Transfer) | Staging folder monitoring (`%TEMP%`, `Public`) |
| **Event ID 12/13/14**| Registry Event | T1112 (Modify Registry) | Persistence run keys & startup modifications |
| **Event ID 19/20/21**| WMI Event | T1546.003 (WMI Event Subscription) | Persistent WMI filter/consumer bindings |