#!/usr/bin/env python 

import ftplib
import os
import socket

HOST = 'ftp.redhat.com'
DIRN = 'pub/pub/redhat/dst2007/README'
FILE = 'DSTFAQ2007_final.pdf'

def main():
	try:
		f = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print('ERROR: cannot reach "%s"' % HOST)
		return
	print('*** Connected to host "%s"' % HOST)
	
	try:
		f.login()
	except ftplib.error_perm:
		print('ERROR: cannot login anonymously')
		f.quit()
		return
	print('*** Logged in as "anonymous"')

	try:
		f.cwd(DIRN)
	except ftplib.error_perm:
		print('ERROR: cannot CD to "%s"' % DIRN)
		f.quit()
	print('*** Changed to "%s" folder' % DIRN)

	try:
		loc = open(FILE, 'wb')
		f.retrbinary('RETR %s' % FILE, loc.write)
	except ftplib.error_perm:
		print('ERROR: cannot read file "%s"' % FILE)
		os.unlink(FILE)
	else:
		loc.close()
		print('*** Downloaded "%s" to CWD' % FILE)
	f.quit()

if __name__ == '__main__':
	main()