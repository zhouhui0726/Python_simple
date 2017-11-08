#!/usr/bin/env python 

from cx_Freeze import setup, Executable


setup(name = 'testto exe', 
		version = '0.1',
		description = 'test from py file to exe file',
		executables = [Executable('SerialFrame.py')]
		
	)
		