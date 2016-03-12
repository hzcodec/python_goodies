#   Auther      : Heinz Samuelsson
#   Date        : 2016-03-12
#   File        : server.py
#   Reference   : -
#   Description : Server. Receiving messages.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import os
from socket import *

host   = ""
port   = 13000
buffer = 1024

addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

print "Waiting to receive messages..."

while True:
  (data, addr) = UDPSock.recvfrom(buffer)
  print "Received message:" + data

  if data == "exit":
    break

UDPSock.close()
os._exit(0)
