#CHECKBUTTONS

#PREGUNTAS DE RESUPUESTA MÚLTIPLE

from tkinter import *

raiz = Tk()
raiz.title("Ejemplo")

playa = IntVar()
montaña = IntVar()
turismoRural = IntVar()

def opcionesViaje():
    opcionesEscogida = ""

    if playa.get() == 1:
        opcionesEscogida += " Playa"
    if montaña.get() == 1:
        opcionesEscogida += " montaña"
    if turismoRural.get() == 1:
        opcionesEscogida += " turismoRural"
    textoFinal.config(text=opcionesEscogida)


foto = PhotoImage(file= "descarga.png")
Label(raiz, image=foto).pack()

frame = Frame(raiz)
frame.pack()

Label(frame, text="Elige destinos", width= 50).pack()
Checkbutton(frame, text="Playa", variable= playa, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",variable= montaña, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable= turismoRural, onvalue = 1, offvalue = 0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

raiz.mainloop()


"""
VERSIÓN REDUCIDA


from tkinter import *

raiz = Tk()
raiz.title("Ejemplo")

frame = Frame(raiz).pack()

playa = IntVar()
montaña = IntVar()
turismoRural = IntVar()

def funcion():
    textoPantalla = ""
    if playa.get() == 1:
        textoPantalla += " Playa"
    else:
        pass
    textoFinal.config(text=textoPantalla)


Checkbutton(frame, text="Playa", onvalue= 1, offvalue = 0, variable = playa, command=funcion).pack()


textoFinal = Label(frame)
textoFinal.pack()



raiz.mainloop()

"""