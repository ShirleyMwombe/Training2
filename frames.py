# frame = rectangular container to hold and group things

from tkinter import *

window = Tk()

frame = Frame(window, bg='yellow', bd=5, relief=SUNKEN)
frame.pack(side=TOP)
# frame.place(x=15, y=15)

button = Button(frame, text='A', font=('Consolas', 15)).pack(side=TOP)
button = Button(frame, text='B', font=('Consolas', 15)).pack(side=LEFT)
button = Button(frame, text='C', font=('Consolas', 15)).pack(side=LEFT)
button = Button(frame, text='D', font=('Consolas', 15)).pack(side=LEFT)

window.mainloop()
