# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ['pizza', 'hotdog', 'burger']


def order():
    if x.get() == 0:
        print("You ordered pizza!")
    elif x.get() == 1:
        print("You ordered a hamburger!")
    elif x.get() == 2:
        print("You ordered a hotdog!")
    else:
        print("huh?")

window = Tk()

pizza = PhotoImage(file='pizza.png')
hotdog = PhotoImage(file='hotdog.png')
burger = PhotoImage(file='humburger.png')

foodimages = [pizza,hotdog,burger]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index],
                              variable=x,  # groups radiobuttons together if they share the same variable
                              value=index,  # assigns each radiobutton a different value
                              padx=25,
                              font=('Impact', 20),
                              image=foodimages[index],  # adds images to radio button according to the index
                              compound=LEFT,            # that we are currently on in the for loop
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()
