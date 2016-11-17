#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import logging
import os

PORT = int(os.getenv('SERVER_PORT'))

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

httpd.serve_forever()
