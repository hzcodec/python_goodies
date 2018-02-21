# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : class_context2.py
# Reference   : http://arnavk.com/posts/python-context-managers/
# Description : Not working example. Need a server to connect to ...
#
# Python ver  : Python 2.7

import socket

class SomeProtocol:

    def __init__(self, host, port):
        print '__init__ host:{}, port:{}'.format(host, port)
        self.host = host
        self.port = port

    def __enter__(self):
        print '__enter__' 
        self._client = socket.socket()
        self._client.connect((self.host, self.port))
        return self

    def __exit__(self, exception, value, traceback):
        print '__exit__'
        self._client.close()

    def send(self, payload):
        pass

    def receive(self):
        pass


host = '127.0.0.1'
#host = socket.gethostname()
port = 8888


with SomeProtocol(host, port) as protocol:
     protocol.send(['get', signal])
     result = protocol.receive()

