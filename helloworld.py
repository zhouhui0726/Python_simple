#!/usr/bin/python3


from functools import partial 
import tkinter

root = tkinter.Tk()


MyButton = partial(tkinter.Button, root, fg = 'white', bg = 'gray')

b1 = MyButton(text = 'Button 1', command = root.quit)
b2 = MyButton(text = 'Button 2', command = root.quit)

qb = MyButton(text = 'Quit', bg = 'blue', command = root.quit)

b1.pack()
b2.pack()

qb.pack(fill=tkinter.X, expand = True)
root.title("PFAs!")
root.mainloop()

		
