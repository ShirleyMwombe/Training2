# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

pic = PhotoImage(file='orange.PNG')
couch = Label(window, text='Its a Couch',
            font=('Calibri', 45, 'bold'),
            fg='green',  # text colour
            bg='yellow',  # background colour
            relief=RAISED,  # border style
            bd=10,  # border width
            padx=20,  # space from x & y
            pady=20,
            image=pic,
            compound="bottom")
couch.pack()  # label name.pack() to display the label
# couch.place(x=0, y=0)  # position the label in the window


window.mainloop()
