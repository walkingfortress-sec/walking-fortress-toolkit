#!/usr/bin/env python3
"""
Walking Fortress - Automated Threat Intelligence Ingestion Engine
Fetches external IOC feeds (AlienVault OTX / MISP / Mock API) and populates
Splunk lookup tables for real-time correlation against endpoint telemetry.
"""

import csv
import datetime
import os
import sys

LOOKUP_FILE = "threat_intel/threat_intel_lookup_template.csv"

def append_ioc_record(ip, domain, file_hash, threat_actor, confidence, category):
    """Appends a validated IOC record to the local SIEM lookup table."""
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    
    file_exists = os.path.exists(LOOKUP_FILE)
    
    with open(LOOKUP_FILE, mode='a', newline='') as csv_file:
        fieldnames = ['ip', 'domain', 'file_hash', 'threat_actor', 'confidence_score', 'category', 'first_seen']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
            
        writer.writerow({
            'ip': ip,
            'domain': domain,
            'file_hash': file_hash,
            'threat_actor': threat_actor,
            'confidence_score': confidence,
            'category': category,
            'first_seen': timestamp
        })
    print(f"[+] Successfully appended IOC: IP={ip} Hash={file_hash} Actor={threat_actor}")

if __name__ == "__main__":
    print("[*] Walking Fortress Threat Intel Feed Ingester Active.")
    # Simulated feed pull demonstration
    append_ioc_record(
        ip="192.168.100.200", 
        domain="malicious-exfil-node.ru", 
        file_hash="4a5b6c7d8e9f0123456789abcdef0123456789abcdef0123456789abcdef0123", 
        threat_actor="UNC2452", 
        confidence=95, 
        category="Egress_Endpoint"
    )
    print(f"[+] Lookup table updated cleanly at {LOOKUP_FILE}")