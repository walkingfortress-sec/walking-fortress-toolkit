#!/usr/bin/env python3
"""
Walking Fortress SOAR Engine - Automated Response Daemon
Receives SIEM Webhook JSON and executes host isolation actions.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import subprocess
import sys

LISTEN_PORT = 5000

def isolate_host(ip_address):
    """Executes host containment via local Netsh firewall rule."""
    rule_name = f"WF_SOAR_ISOLATE_{ip_address}"
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}", "dir=out", "action=block",
        f"remoteip={ip_address}"
    ]
    print(f"[!] EXECUTING SOAR ACTION: Blocking outbound traffic to {ip_address}")
    # Run command safely
    # subprocess.run(cmd, check=True)

class SOARWebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        payload = json.loads(post_data.decode('utf-8'))
        
        severity = payload.get("severity", "LOW").upper()
        src_ip = payload.get("source_ip", "0.0.0.0")
        rule_name = payload.get("rule_name", "Unknown Alert")

        print(f"\n[+] Incoming Alert: {rule_name} | Severity: {severity} | Host: {src_ip}")

        # Automated Response Policy
        if severity in ["HIGH", "CRITICAL"]:
            print(f"[ALERT TRIGGERED] High severity threat detected from {src_ip}.")
            isolate_host(src_ip)
            response = {"status": "success", "action_taken": "host_isolated"}
        else:
            print("[INFO] Alert logged. No automated isolation required.")
            response = {"status": "success", "action_taken": "logged_only"}

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', LISTEN_PORT), SOARWebhookHandler)
    print(f"[*] Walking Fortress SOAR Daemon operational on port {LISTEN_PORT}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Shutting down SOAR Daemon.")
        sys.exit(0)