# SOP-03: Phishing & Credential Harvesting Response Playbook

| Step | Action Item | Command / Vector |
|---|---|---|
| **1. Header Triage** | Analyze DKIM, SPF, and DMARC alignment failures on reported inbound emails. | Mail Gateway Log Inspection |
| **2. Payload Analysis** | Detonate attached macro/executable or analyze malicious URL in isolated sandbox environment. | Scapy PCAP Analyzer / Any.Run |
| **3. Identity Isolation** | Force password reset for target accounts; revoke OAuth consent grants matching malicious app IDs. | Azure CLI / Active Directory User Reset |
| **4. Scope Containment** | Search mail server for matching Subject lines or Sender IPs and purge remaining instances across tenant. | Exchange PowerShell `Search-Mailbox -DeleteContent` |