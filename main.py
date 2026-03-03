from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
from pathlib import Path

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>GitHub Actions & Docker</title>
        </head>
        <body>
            <h1>hello!</h1>
            <p>If you want to learn more about GitHub Actions and Docker, go here: <a href="https://docs.docker.com/guides/gha/">https://docs.docker.com/guides/gha/</a></p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), MyHandler)
    print('Server running on http://localhost:8000')
    server.serve_forever()