# Author      : Heinz Samuelsson
# Date        : Fri Mar 25 10:38:15 CET 2016
# File        : class_context2.py
# Reference   : http://arnavk.com/posts/python-context-managers/
# Description : Not working example.
#
# Python ver  : Python 2.7

import socket

class SomeProtocol:

     def __init__(self, host, port):
          self.host, self.port = host, port

     def __enter__(self):
          self._client = socket.socket()
          self._client.connect((self.host, self.port))
          return self

     def __exit__(self, exception, value, traceback):
          self._client.close()

     def send(self, payload): ...

     def receive(self): ...


host = '127.0.0.1'
port = 8888

with SomeProtocol(host, port) as protocol:
     protocol.send(['get', signal])
     result = protocol.receive()
