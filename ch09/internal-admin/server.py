# 社内のネットワークの中だけで使う管理用のサービス（外からは開けない想定）
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"service": "internal-admin", "flag": "FLAG{ssrf}"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 9000), Handler).serve_forever()
