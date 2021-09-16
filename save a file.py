from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\hp\\PycharmProjects\\Training2',
                                    defaultextension='.txt',
                                    filetypes=[('text file', '.txt'),
                                               ('html file', '.html'),
                                               ('all files', '.*')])
    if file is None:  # no exceptions
        return
    #filetext = text.get(1.0, END)
    filetext = input('Enter anything: ') # input text through console window
    file.write(filetext)
    file.close()


window = Tk()

button = Button(window, text='save',
                command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
