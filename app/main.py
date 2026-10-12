from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {
                "status": "healthy",
                "application": "devops-cicd-kubernetes"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"DevOps CI/CD application is running!")
        else:
            self.send_error(404, "Not Found")

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Application listening on port 8000")
server.serve_forever()
