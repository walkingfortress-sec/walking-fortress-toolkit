# Walking Fortress Enterprise Security Operations Framework

## Core Architectural Pillars

1. **Endpoint & Active Directory Telemetry (`identity/`, `persistence/`, `baselines/`)**
   * Sysmon Event ID ID-to-MITRE mapping baseline.
   * PowerShell ScriptBlock (4104) and Kerberos TGS (4769) detection logic.

2. **Automated Response & SOAR Infrastructure (`soar/`, `tools/`)**
   * Daemon-based automated network isolation (`auto_responder_daemon.py`).
   * PCAP automated payload and DNS triage script (`pcap_analyzer.py`).

3. **Cloud, Container & Emulation Defense (`cloud_security/`, `container_security/`, `emulation/`)**
   * AWS IAM & Azure AD illicit consent grant detection queries.
   * Kubernetes & Docker runtime threat detection via Falco.
   * Atomic Red Team threat emulation harness (`atomic_red_team_execution.ps1`).

4. **CI/CD & Quality Assurance (`.github/workflows/`, `tests/`)**
   * GitHub Actions workflow validating detection rule syntax on pull requests.
   * Automated SIEM regression testing runner using synthetic JSON logs.