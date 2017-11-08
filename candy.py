#!/usr/bin/env python

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

lock = Lock()
MAX = 5
canfytray = BoundedSemaphore(MAX)


def refill():
	lock.acquire()
	print('Refilling candy...')
	try:
		canfytray.release()
	except ValueError:
		print('full, skipping...')
	else:
		print('OK')
	lock.release()

def buy():
	lock.acquire()
	print('Buying candy...')
	if canfytray.acquire(False):
		print('OK')
	else:
		print('empty, skpping')
	lock.release()

def producer(loops):
	print('producer loops:', loops)
	for i in range(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	print('consumer loops:', loops)
	for i in range(loops):
		buy()
		sleep(randrange(3))

def _main():
	print('starting at:', ctime())
	nloops = randrange(2, 6)
	print('THE CANDY MACHINE (full with %d bars)!' % MAX)
	Thread(target=consumer, args=(randrange(nloops, 
			nloops+MAX+2),)).start()
	Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
	print('all DONE at:', ctime())

if __name__ == '__main__':
	_main()
