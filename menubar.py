from tkinter import *


def openFile():
    print('File Opened!')


def saveFile():
    print('File saved!')


def copyFile():
    print('File copied!')


def cutFile():
    print('File cut!')


def pasteFile():
    print('File pasted!')


window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=('calibri',15))
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit)

editmenu = Menu(menubar, tearoff=0, font=('calibri',15))
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_cascade(label='Copy', command=copyFile)
editmenu.add_cascade(label='Cut', command=cutFile)
editmenu.add_cascade(label='Paste', command=pasteFile)

window.mainloop()
