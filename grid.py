from tkinter import *

window = Tk()

firstNamelabel = Label(window, text='First Name').grid(row=0, column=0)
firstNameentry = Entry(window).grid(row=0, column=1)

lastNamelabel = Label(window, text='Last Name').grid(row=1, column=0)
lastNameentry = Entry(window).grid(row=1, column=1)

emailLabel = Label(window, text='Email').grid(row=2, column=0)
emailEntry = Entry(window).grid(row=2, column=1)

submitButton = Button(window, text='Submit').grid(row=3, column=0, columnspan=2)
window.mainloop()
