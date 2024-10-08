from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import json
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(SimpleHTTPRequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        print(self.path)
        if self.path == '/profile-update':
            request_data = self.getPostData()
            subprocess.Popen([".venv/bin/python", "src/profile_update.py",
                              "-d", request_data,
                              "symbol"], stdout=open('subprocess.log', 'a'), stderr=open('subprocess.errlog', 'a'))

            response = bytes('{"update": "srarted"}', "utf-8") 

            self.send_response(200) 
            self.send_header('Content-type','application/json')
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response) 

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

#httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd = HTTPServer(('test.vampling.com', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="/etc/letsencrypt/live/test.vampling.com/privkey.pem", 
        certfile='/etc/letsencrypt/live/test.vampling.com/fullchain.pem', server_side=True)
httpd.serve_forever()
