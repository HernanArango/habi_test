from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import config
from modules.property.property import get_properties
import urllib


class ServiceHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_path = urllib.parse.urlsplit(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        data = get_properties(params)

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


server = HTTPServer((config.BASE_URL, config.PORT), ServiceHandler)
print(f"Server running in http://{config.BASE_URL}:{config.PORT}")
server.serve_forever()
