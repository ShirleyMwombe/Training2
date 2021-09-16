from tkinter import *   # import window module
from tkinter import ttk  # import notebook module

window = Tk()

notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays

tab1 = Frame(notebook)  # new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1, text='Tab1')
notebook.add(tab2, text='Tab2')

Label(tab1, text='This is Tab One', width=50, height=25).pack()
Label(tab2, text='This is Tab One', width=50, height=25).pack()

notebook.pack(expand=True, fill='both')  # expand to fill space not used

window.mainloop()
