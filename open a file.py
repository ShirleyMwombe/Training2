from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\hp\\PycharmProjects\\Training2",
                                          title='open file?',
                                          filetypes=(('text files', "*.txt"), ('all files', "*.*")))
    file = open(filepath)
    print(file.read())
    file.close()


window = Tk()

button = Button(window, text='open',
                command=openfile)
button.pack()

window.mainloop()
