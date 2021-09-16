# widget = GUI elements : text boxes, images, buttons, labels etc
# windows = container to hold or contain these images

from tkinter import *  #import tkinter module

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")  # specify window size
window.title('WNDW')

icon = PhotoImage(file='orange.png')
window.iconphoto(True,icon)
window.config(background='purple')  # use colour name/#code
window.mainloop()   # display window