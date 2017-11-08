#!/usr/bin/env python 
import threading
from time import sleep, ctime
def loop0():
	print('start loop 0 at:', ctime())
	sleep(4)
	print('loop 0 done at:', ctime())

def loop1():
	print('start loop 1 at:', ctime())
	sleep(2)
	print('loop 1 done at:', ctime())
def main():
	print('starting at:', ctime())
	threading._start_new_thread(loop0, ())
	threading._start_new_thread(loop1, ())
	print('all thread start at:', ctime())
	sleep(6)
	print('all DONE at:', ctime())
if __name__ == '__main__':
	main()