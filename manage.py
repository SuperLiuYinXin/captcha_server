# -*- coding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app.server import app
import sys 

if len(sys.argv) >= 2:
	port = sys.argv[1]
	port = int(port)
else:
	print('将选择默认端口号, 5000')
	port = 5000

http_server = HTTPServer(WSGIContainer(app))
print('server start on port %d' % port)
http_server.listen(port)
IOLoop.instance().start()
