from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import datetime

PORT = 5000

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"\n[!] ALERT RECEIVED AT [{timestamp}]")
        print("-" * 50)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
            print(json.dumps(payload, indent=4))
        except json.JSONDecodeError:
            print(post_data.decode('utf-8'))
            
        print("-" * 50)
        
        # Send a 200 OK response back to the sender
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"status": "success", "message": "Alert received and logged by Walking Fortress Listener"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run_server():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f"[*] Walking Fortress Webhook Listener active on http://127.0.0.1:{PORT}...")
    print("[*] Waiting for incoming SIEM alerts... (Press Ctrl+C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Shutting down webhook listener.")
        httpd.server_close()

if __name__ == '__main__':
    run_server()