#!/usr/bin/env python

from tkinter import *

top = Tk()

hello = Label(top, text='Hello World!')
hello.pack()

quit = Button(top, text='QUIT', command = top.quit, 
		bg = 'red', fg = 'white')
quit.pack(fill = X, expand = 1)
mainloop()