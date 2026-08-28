# Enterprise SOC Laboratory Architecture

```mermaid
flowchart TD
    subgraph Host_Layer [Host Telemetry Layer]
        A[Windows Server 2022] -->|Sysmon Logs / Event 4104| B[Splunk Universal Forwarder]
    end

    subgraph Network_Layer [Network Telemetry Layer]
        C[Zeek / Suricata IDS] -->|conn.log / dns.log / eve.json| D[Logstash / Forwarder]
    end

    subgraph Analytics_Layer [SIEM & Detection Engine]
        B --> E[Splunk Enterprise]
        D --> E
        E -->|Correlation SPL| F[Alert Engine]
    end

    subgraph Automation_Layer [Incident Response & Webhooks]
        F -->|POST Webhook JSON| G[Local Python Listener]
        G --> H[Automated IR Playbook Execution]
    end