#!/usr/bin/env python 
from socket import *

from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

BUFSIZE = 1024


udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print('waiting for message...')
	data, addr = udpSerSock.recvfrom(BUFSIZE)
	udpSerSock.sendto(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'), addr)

	print('...reeived from and returned to:', addr)
udpSerSock.close()