from tkinter import *
from tkinter import ttk

root = Tk()

selected = StringVar()

def selec():
    if(selected.get()=='1'):
        lab.config(text="Opción 1")
    elif(selected.get()=='2'):
        lab.config(text="Opción 2")
    elif(selected.get()=='3'):
        lab.config(text="Opción 3")

def borrado():
    selected.set("")
    lab.config(text="")

r1 = ttk.Radiobutton(root, text="Opción 1", value='1', variable=selected, command=selec).grid(column=1, row=0, pady=5, padx=5)
r2 = ttk.Radiobutton(root, text="Opción 2", value='2', variable=selected, command=selec).grid(column=1, row=1, pady=5, padx=5)
r3 = ttk.Radiobutton(root, text="Opción 3", value='3', variable=selected, command=selec).grid(column=1, row=2, pady=5, padx=5)
borrar = ttk.Button(root, text="Borrar", command=borrado).grid(column=1, row=3, pady=5, padx=5)

lab = Label(root)
lab.grid(column=1, row=4)


root.mainloop()