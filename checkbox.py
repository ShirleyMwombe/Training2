from tkinter import *


def display():
    if x.get() == 1:
        print('Agreed :)')
    else:
        print('Not Agreed :(')

window = Tk()

x = IntVar()  # change to BooleanVar() if True & False

check_button = Checkbutton(window,
                           text='I Agree',
                           font=('Arial', 15),
                           fg='#00ff00',
                           bg='black',
                           variable=x,
                           onvalue=1,  # can be True & False
                           offvalue=0,
                           command=display,
                           padx=25,
                           pady=10)
check_button.pack()
window.mainloop()
