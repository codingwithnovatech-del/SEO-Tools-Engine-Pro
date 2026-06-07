#!/usr/bin/env python3
"""CORS proxy for Open PageRank API - run alongside HTTP server"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import json

OPR_API_KEY = "40skw8k84cgowcswwk80ocok80occsk0kw0cw8so"

class ProxyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/opr?'):
            qs = self.path.split('?', 1)[1]
            from urllib.parse import parse_qs, urlencode
            params = parse_qs(qs)
            domain = params.get('domain', [''])[0]
            if not domain:
                self._send_json({'error': 'missing domain'}, 400)
                return
            api_url = f'https://openpagerank.com/api/v1.0/getPageRank?domains[]={domain}'
            req = urllib.request.Request(api_url, headers={'API-OPR': OPR_API_KEY})
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode())
                    self._send_json(data)
            except Exception as e:
                self._send_json({'error': str(e)}, 502)
        else:
            self.send_response(404)
            self.end_headers()

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

if __name__ == '__main__':
    port = 8001
    server = HTTPServer(('0.0.0.0', port), ProxyHandler)
    print(f'OPR Proxy running on http://localhost:{port}')
    server.serve_forever()
