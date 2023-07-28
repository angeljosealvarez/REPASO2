from tkinter import *

raiz = Tk()
raiz.title("Ejemplo")

frame = Frame(raiz)
frame.pack()

playa = IntVar()
montaña = IntVar()
turismoRural = IntVar()

def opcionesViaje():

    opcionEscogida = ""
    
    if playa.get() == 1:
        opcionEscogida += " Playa"
    if montaña.get() == 1:
        opcionEscogida += " montaña"
    if turismoRural.get() == 1:
        opcionEscogida += " turismoRural"
    textoFinal.config(text = opcionEscogida)


foto = PhotoImage(file = "descarga.png")
Label(raiz, image=foto).pack()

Label(frame, text="Elige destinos", width=50).pack()
Checkbutton(frame, text="Playa", variable= playa, onvalue= 1, offvalue = 0, command= opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable= montaña, onvalue= 1, offvalue = 0, command= opcionesViaje).pack()
Checkbutton(frame, text="turismoRural", variable= turismoRural, onvalue= 1, offvalue = 0, command= opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()
raiz.mainloop()