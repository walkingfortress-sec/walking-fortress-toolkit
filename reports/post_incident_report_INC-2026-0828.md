# Executive Post-Incident Report: INC-2026-0828

**Target Host:** `DC01.walkingfortress.local` | **Vector:** Kerberoasting & Scheduled Task Persistence | **Severity:** Critical  

## Executive Summary
On August 28, 2026, the Walking Fortress SIEM detected an unauthorized Kerberoasting attempt (T1558.003) executed via PowerShell, followed by a Scheduled Task creation (T1053.005). The automated SOAR daemon ingested the critical alert payload and issued a host network isolation rule within 10 seconds of initial detection, preventing domain-wide credential compromise.

## Actionable Recommendations
1. **Enforce AES Encryption:** Disable legacy RC4-HMAC encryption (`0x17`) for Kerberos TGS requests domain-wide.
2. **Service Account Hardening:** Require 25+ character complex passwords for all SPN-associated service accounts.# Executive Post-Incident Report: INC-2026-0828

**Target Host:** `DC01.walkingfortress.local` | **Vector:** Kerberoasting & Scheduled Task Persistence | **Severity:** Critical  

## Executive Summary
On August 28, 2026, the Walking Fortress SIEM detected an unauthorized Kerberoasting attempt (T1558.003) executed via PowerShell, followed by a Scheduled Task creation (T1053.005). The automated SOAR daemon ingested the critical alert payload and issued a host network isolation rule within 10 seconds of initial detection, preventing domain-wide credential compromise.

## Actionable Recommendations
1. **Enforce AES Encryption:** Disable legacy RC4-HMAC encryption (`0x17`) for Kerberos TGS requests domain-wide.
2. **Service Account Hardening:** Require 25+ character complex passwords for all SPN-associated service accounts.