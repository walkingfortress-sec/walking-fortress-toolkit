# Network Visibility Architecture: Zeek vs. Suricata

| Feature | Suricata (IDS/IPS) | Zeek (NSM) |
|---|---|---|
| **Core Function** | Alerting & Packet Inspection | Transaction Logging & Protocol Parsing |
| **Output Type** | `eve.json` (Alert-focused) | `conn.log`, `dns.log`, `http.log`, `ssl.log` |
| **Primary Use Case** | Known-bad signature enforcement | Threat hunting, baselining, and forensics |
| **Rule Engine** | Snort-style signatures (`alert tcp...`) | Event-driven scripting language (`.zeek`) |

## Splunk Telemetry Correlation Pair
* **Host Layer:** `Sysmon EventCode 3` (Network Connection)
* **Network Layer:** `zeek:conn` log (`id.orig_h`, `id.resp_h`, `id.resp_p`)
* **DNS Resolution:** `zeek:dns` log (`query`, `answers`, `rcode_name`)