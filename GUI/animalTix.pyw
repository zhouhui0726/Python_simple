#!/usr/bin/env python 

from tkinter import Label, Button, END, X
from tkinter.tix import Tk, Control, ComboBox

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top, text='Animals (in pairs; min: pair, max: dozen)')
lb.pack()

ct = Control(top, label='Number:', integer=True, max = 12, min = 0, value = 2, step= 1)
ct.label.config(font='Helvetica -14 bold')
ct.pack()

cb = ComboBox(top, label='Type:', editable=True)
for animal in ('dog', 'cat', 'hamster', 'python'):
	cb.insert(END, animal)
cb.pack()

qb = Button(top, text='QUIT', command=top.quit, bg='red', fg = 'white')
qb.pack(fill=X, expand = True)
top.mainloop()