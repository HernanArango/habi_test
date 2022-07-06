from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import config


class ServiceHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        data = ["server running"]
        self.wfile.write(json.dumps(data).encode())


server = HTTPServer((config.BASE_URL, config.PORT), ServiceHandler)
print(f"Server running in http://{config.BASE_URL}:{config.PORT}")
server.serve_forever()
