#!/usr/bin/env python


import nntplib
import socket

HOST = 'news.gmane.org'
GRNM = 'gmane.comp.python.committers'
USER = 'wesley'
PASS = 'youllNeverGuess'

def main():
	try:
		n = nntplib.NNTP(HOST)
	except socket.gaierror as e:
		print('ERROR: cannot reach host "%s"' % HOST)
		print('    ("%s")' % str(e))
		return
	except nntplib.NNTPPermanentError as e:
		print('ERROR: access denied on "%s"' % HOST)	
		print('    ("%s")' % str(e))
	print('*** Connected to host "%s"' % HOST)


	try:
		rsp, ct , fst, lst, grp = n.group(GRNM)
	except nntplib.NNTPTemporaryError as ee:
		print('ERROR: cannot load group "%s"' % GRNM)
		print('     ("%s)' % str(ee))
		print('     Server may require authentication')
		print('     Uncomment login line above')
		n.quit()
		return
	except nntplib.NNTPTemporaryError as ee:
		print('ERROR: group "%s" unavailable' % GRNM)
		print('     ("%s)' % str(ee))
		n.quit()
		return
	print('*** Found newsgroup "%s"' % GRNM)
	rng = '%s-%s' % (lst, lst)
	rsp, frm = n.xhdr('from', rng)
	rsp, sub = n.xhdr('sunject', rng)
	rsp, dat = n.xhdr('date', rng)
	print('''*** Found last article (%s):
		from: %s
		Subject: %s
		Date: %s
		''' % (lst, frm, sub, dat))
	rsp, anum, mid, data = n.body(lst)
	displayFirst20(data)
	n.quit()
def displayFirst20(data):
	print('*** First (<= 20) meaningful lines:\n')
	count = 0
	lines = (line.strip() for line in data)
	lastBlank  = True
	for line in lines:
		lower = line.lower()
		if(lower.startswith('>') and not \
			lower.startswith('>>>')) or \
			lower.startswith('|') or \
			lower.startswith('in artcle') or \
			lower.endswith('write:') or \
			lower.endswith('wrote:'):
			continue
		if not lastBlank or (lastBlank and line):
			print('    %s' % line)
			if line:
				count += 1
				lastBlank = False
			else:
				lastBlank = True
		if count == 20:
			break
if __name__ == '__main__':
	main()