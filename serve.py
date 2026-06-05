#!/usr/bin/env python3
import socket
import http.server
import socketserver
import os

os.chdir(os.path.dirname(__file__) or '.')

def find_and_serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        port = s.getsockname()[1]

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving on port {port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    find_and_serve()
