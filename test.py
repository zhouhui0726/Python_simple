#usr/bin/env python2/3
import re
import os
from distutils.log import warn as printf


with os.popen('tasklist -nh', 'r') as f:
	for eachLine in f:
		printf(re.findall(r'([\w.]+(?: [\w.]+)*)\s\s+(\d+) \w+\s\s+\d+\s\s+([\d,]+ K)',\
		 eachLine.strip()))