# Automated SOAR Execution Workflow

```mermaid
sequenceDiagram
    autonumber
    participant Endpoint as Compromised Host
    participant SIEM as Splunk / Wazuh SIEM
    participant SOAR as Python SOAR Daemon
    participant Firewall as Host/Net Firewall

    Endpoint->>SIEM: Generates High-Severity Telemetry (T1003.001 / T1558.003)
    SIEM->>SOAR: HTTP POST Alert Payload (JSON, Severity=CRITICAL)
    SOAR->>SOAR: Parse Severity & Source IP
    SOAR->>Firewall: Execute Netsh Outbound Block Rule
    Firewall-->>SOAR: Rule Applied (Host Isolated)
    SOAR-->>SIEM: 200 OK (Action Taken: host_isolated)