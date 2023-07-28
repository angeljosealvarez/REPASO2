#WIDGET ENTRY
"""
Los widget entry son widgets cuya función es que el usuario pueda añadir texto
"""
from tkinter import *

raiz = Tk()
miFrame = Frame(raiz, width=500, height=500)
miFrame.pack()

cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=1, column=2)

cuadroContraseña = Entry(miFrame)
cuadroContraseña.grid(row=4, column=2)
cuadroContraseña.config(fg="blue", justify="center", show="*") #CAMBIAR COLOR CON FG Y LA ALINEACIÓN DEL TEXTO CON JUSTIFY

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=2)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=2)


nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=1, sticky="w", pady=10, padx=10) #SE ENCARGA DE PONER LA LABEL EN UN LUGAR ESPECÍFICO (STICKY)

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3, column=1, sticky="w", pady=10, padx=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=1, sticky="w", pady=10, padx=10)

contraseñaLabel = Label(miFrame, text="Contraseña: ")
contraseñaLabel.grid(row=4, column=1, sticky="w", pady=10, padx=10)


#ALINEACIONES (SI QUIERO QUE EL NOMBRE, DIRECCIÓN Y APELLIDO ESTÉN A LA DERECHA, IZQUIERDA, ARRIBA O ABAJO) CON LA FUNCIÓN STICKY
"""
para usar la función sticky:
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=3, column=1, sticky="w")

PADY y PADX
Se encarga de mantener la distancia entre un label con otro manteniendo proporcionalidad entre un eje x o y, dependiendo de si se usa padx o pady
"""

raiz.mainloop()

from tkinter import *
raiz = Tk()

miFrame = Frame(raiz, width=500, height=500)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=0, column=1)

nombreLabel=Label(miFrame, text="Nombre: ")
#No se usa place para evitar que se superpongan los elementos
nombreLabel.grid(row=0, column=0)

raiz.mainloop() 