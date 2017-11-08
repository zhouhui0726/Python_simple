#!/usr/bin/env python 

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
import re, os

tlds = ('com', 'end', 'net', 'org', 'gov')

f = open('redata.txt', 'w+')

for i in range(randrange(5, 11)):
	dint = randrange(maxsize)
	dstr = ctime(dint)
	llen = randrange(4, 8)
	login = ''.join(choice(lc) for j in range(llen))
	dlen = randrange(llen, 13)
	dom = ''.join(choice(lc) for j in range(dlen))
	f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dstr, login,
		dom, choice(tlds), dint, llen, dlen))

f.seek(os.SEEK_SET)
for readline in f:
	print(readline, end='')

f.close()