#   Auther      : Heinz Samuelsson
#   Date        : 2016-03-12
#   File        : client.py
#   Reference   : -
#   Description : 8 Clickable switches.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import os
from socket import *

host = "127.0.0.1" # set IP address to local host
port = 13000
addr = (host, port)

UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
  data = raw_input("Enter message (exit = quit: ")
  UDPSock.sendto(data, addr)

  if data == "exit": 
    break

UDPSock.close()
os._exit(0)
