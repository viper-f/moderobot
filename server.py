from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print(self.path)
        if self.path == '/profile-update':
            request_data = self.getPostData()
            subprocess.Popen([".venv/bin/python", "src/profile_update.py",
                              "-d", request_data['data'],
                              "symbol"], stdout=open('subprocess.log', 'a'), stderr=open('subprocess.errlog', 'a'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Updating. Wait a minute')

        if self.path == '/login':
            request_data = self.getPostData()
            subprocess.Popen([".venv/bin/python", "src/login.py",
                              "-d", request_data,
                              "symbol"], stdout=open('subprocess.log', 'a'), stderr=open('subprocess.errlog', 'a'))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Logging in')

    def getPostData(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        return post_data.decode('utf-8')

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()