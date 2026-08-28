#!/usr/bin/env python3
"""
Walking Fortress - Automated PCAP Telemetry Extractor
Parses raw packet captures for high-risk DNS queries and cleartext HTTP POST payloads.
"""

from scapy.all import rdpcap, DNS, DNSQR, IP, TCP, Raw
import sys

def analyze_pcap(pcap_path):
    print(f"[*] Analyzing PCAP File: {pcap_path}")
    packets = rdpcap(pcap_path)
    
    for pkt in packets:
        # Check for suspicious DNS queries (>60 characters)
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            query = pkt[DNSQR].qname.decode('utf-8', errors='ignore')
            if len(query) > 60:
                src = pkt[IP].src
                print(f"[!] Suspicious Large DNS Query ({len(query)} bytes) from {src}: {query}")

        # Check for HTTP POST Data (Potential Egress/C2)
        if pkt.haslayer(TCP) and pkt.haslayer(Raw):
            payload = pkt[Raw].load.decode('utf-8', errors='ignore')
            if "POST " in payload:
                src = pkt[IP].src
                dst = pkt[IP].dst
                print(f"[!] Outbound HTTP POST Detected from {src} -> {dst}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 pcap_analyzer.py <file.pcap>")
        sys.exit(1)
    analyze_pcap(sys.argv[1])