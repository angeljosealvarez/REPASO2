from tkinter import *
raiz = Tk()

varOpcion = IntVar()

Label(raiz, text="Género").pack()

def imprimir():

    if varOpcion == 1:
        etiqueta.config(text="Has elegido masculino")
    elif varOpcion == 2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otras opciones")

Radiobutton(raiz, text="Masculino", variable= varOpcion, value= 1).pack()
Radiobutton(raiz, text="Femenino", variable= varOpcion, value= 2).pack()
Radiobutton(raiz, text="Otras opciones", variable= varOpcion, value= 3).pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()