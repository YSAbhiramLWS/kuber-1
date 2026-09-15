from http.server import BaseHTTPRequestHandler, HTTPServer


class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = "Hello from SMO Server!"

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())


server_address = ("0.0.0.0", 8080)

server = HTTPServer(server_address, ServerHandler)

print("SMO Server is running on port 8080...")

server.serve_forever()