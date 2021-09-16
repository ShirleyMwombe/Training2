# button = you click it, then it does stuff

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)
    #print('You clicked me!')

window = Tk()

photo = PhotoImage(file='orange.png')
button = Button(window, text='click here',
                command=click,
                font=('consolas', 15, 'bold'),
                fg='yellow',
                bg='black',
                activeforeground='#00FF00',
                activebackground='black',
                state=ACTIVE,  #  can be DISABLED
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
