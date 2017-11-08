#!/usr/bin/env  python


from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen, build_opener
from concurrent.futures import ThreadPoolExecutor

REGEX = compile(b'#([\d,]+) in Books') 
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django',
	'0137143419': 'Python Fundamentals',
}
def getRanking(isbn):
	opener = build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	page = opener.open('%s%s' % (AMZN, isbn))
	data = page.read()
	# page.close()
	return str(REGEX.findall(data)[0], 'utf-8')

def _showRanking(isbn):
	print('- %r ranked %s' % (ISBNs[isbn], getRanking(isbn)))

def _main():
	print('AT', ctime(), 'on Amazon...')
	with ThreadPoolExecutor(3) as executor:
		for isbn, ranking in zip(
			ISBNs, executor.map(getRanking, ISBNs)):
			print('- %r ranked %s' % (ISBNs[isbn], ranking))
@register
def _atexit():
	print('all DONE at:', ctime())

if __name__ == '__main__':
	_main()