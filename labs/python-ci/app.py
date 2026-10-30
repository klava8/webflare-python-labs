"""Учебное веб-приложение стандартной библиотеки."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from message import greeting


class Handler(BaseHTTPRequestHandler):
    """Обработчик GET с параметром name."""

    def do_GET(self):
        """Отправить JSON-приветствие или ошибку."""
        name = parse_qs(urlparse(self.path).query).get("name", [""])[0]
        try:
            payload = {"message": greeting(name)}
            status = 200
        except ValueError as error:
            payload = {"error": str(error)}
            status = 400
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8066), Handler).serve_forever()
