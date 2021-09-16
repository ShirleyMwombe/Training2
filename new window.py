from tkinter import *

def createWindow():
    #new_window = Toplevel()  # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    window1 = Tk()                         #Tk() = new independent window
    window.destroy()

window = Tk()

button = Button(window, text='create new window', command=createWindow).pack()

window.mainloop()
