import http.server
import socketserver
import os
import re

PORT = 5000
DIRECTORY = "docs"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.end_headers()
            
            with open(os.path.join(DIRECTORY, 'index.html'), 'r') as f:
                content = f.read()
            
            content = content.replace('{{FIREBASE_API_KEY}}', os.environ.get('FIREBASE_API_KEY', ''))
            content = content.replace('{{FIREBASE_AUTH_DOMAIN}}', os.environ.get('FIREBASE_AUTH_DOMAIN', ''))
            content = content.replace('{{FIREBASE_DATABASE_URL}}', os.environ.get('FIREBASE_DATABASE_URL', ''))
            content = content.replace('{{FIREBASE_PROJECT_ID}}', os.environ.get('FIREBASE_PROJECT_ID', ''))
            content = content.replace('{{FIREBASE_STORAGE_BUCKET}}', os.environ.get('FIREBASE_STORAGE_BUCKET', ''))
            content = content.replace('{{FIREBASE_MESSAGING_SENDER_ID}}', os.environ.get('FIREBASE_MESSAGING_SENDER_ID', ''))
            content = content.replace('{{FIREBASE_APP_ID}}', os.environ.get('FIREBASE_APP_ID', ''))
            
            self.wfile.write(content.encode())
        else:
            super().do_GET()
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server running at http://0.0.0.0:{PORT}/")
        print(f"Serving files from: {DIRECTORY}")
        httpd.serve_forever()
