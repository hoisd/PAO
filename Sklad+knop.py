import Zapasi
from tkinter import *
from tkinter import ttk
root = Tk()
ent = Entry (root,bg="white",fg="black") # Ввод названия позиции
ent.pack()
ent1 = Entry (root,bg="white",fg="black") # Ввод программы выпуска изделий
ent1.pack()
ent2 = Entry (root,bg="white",fg="black") # Ввод периодичности проверки запасов
ent2.pack()
def prinjat(event):
    S1 = Zapasi.Izdelie(ent.get(),int(ent1.get()),int(ent2.get()))
    return S1
    
root.geometry("500x200")
but = ttk.Button(text="Проверка")
but.place(relx=.5, rely=.5, anchor="c", width=200, height=40)

but.bind("<Button-1>",prinjat)

root.mainloop()