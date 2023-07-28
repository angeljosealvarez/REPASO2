#RADIO BUTTONS

#Botones que solo permiten una única selección
from tkinter import *
raiz = Tk()

varOpción= IntVar()

def imprimir():
    #print(varOpción.get())
    if varOpción.get() == 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpción.get() == 2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otras opciones")


Label(raiz, text="Género:").pack()

Radiobutton(raiz, text="Masculino", variable= varOpción, value = 1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable= varOpción, value = 2, command= imprimir).pack()
Radiobutton(raiz, text="Otras opciones", variable= varOpción, value = 3, command= imprimir).pack()


etiqueta= Label(raiz)
etiqueta.pack()

raiz.mainloop()

"""
VERSION REDUCIDA

from tkinter import *
raiz = Tk()

varOpcion = IntVar()

def imprimir():

    if varOpcion.get() == 1:
        textoFinal.config(text="Has elegido masculino")
    elif varOpcion.get() == 0:
        textoFinal.config(text="Has elegido femenino")
    else:
        textoFinal.config()


Radiobutton(raiz, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(raiz, text="Femenino", variable=varOpcion, value=0, command=imprimir).pack()

textoFinal = Label(raiz)
textoFinal.pack()

raiz.mainloop()
"""