from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def OpcViaje():
	opcionEscogida=""
	if(playa.get()==1):
		opcionEscogida+= " Playa"
	if(montagna.get()==1):
		opcionEscogida+= " Montaña"
	if(turismoRural.get()==1):
		opcionEscogida+= " Turismo rural"
	textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="Img_ej_turismo.png")
Label(root, image=foto).pack()

frame=Frame(root).pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=OpcViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=OpcViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=OpcViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()










root.mainloop()