from tkinter import *
from tkinter import ttk
def vzyat(event):
    print('ГООООООООЛ!')
root = Tk()
root.geometry("500x200")
but = ttk.Button(text="С новой гойдой!")
but.place(relx=.5, rely=.5, anchor="c", width=200, height=40)

but.bind("<Button-1>",vzyat)

root.mainloop()