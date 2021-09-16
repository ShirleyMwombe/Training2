from tkinter import *


def submit():
    print('The temperature is', scale.get(), 'degrees C')

window = Tk()

#hotImage = PhotoImage(file='hot.jpg')
#hotLabel = Label(image=hotImage)
#hotLabel.pack()

scale = Scale(window, from_=100, to=0,
              length=400,
              orient=VERTICAL,  # orientation of scale
              font=('Consolas',10),
              tickinterval=10,  # numeric indicators on the scale
              showvalue=1,  # shows or hides current value
              resolution=5,  # increment of slider
              troughcolor='blue',
              fg='red',
              bg='black')

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

#coldImage = PhotoImage(file='cold.png')
#coldLabel = Label(image=coldImage)
#coldLabel.pack()

button = Button(window, text='submit',
                command=submit)
button.pack()

window.mainloop()
