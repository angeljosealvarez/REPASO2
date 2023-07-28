#LABELS
#Texto que no se puede modificar
"""
LABEL

SINTAXIS: Label(contenedor (lugar donde se encontrará el label), opciones)
miLabel = Label(miFrame, text="Hola alumnos de Python", fg)
miLabel.pack() AL USAR PACK EL CONTENEDOR (EN ESTE CASO MIFRAME) ADAPTA LAS DIMENSIONES DEL LABEL, PARA QUE NO SUCEDA SE DEBE DE SUSTITUIT PACK():
miLabel.place(x=100,y=200) x obedece la distancia desde el borde izquierdo e y obedece la distancia desde el borde superior hacia el texto
"""

from tkinter import * #import tkinter hace lo mismo
root = Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()
# miImagen= PhotoImage(file="CAMISETA DE OSO.png")
miLabel= Label(miFrame, text="Hola alumnos de python", fg="blue", font=("Comic Sans MS", 18)).place(x=100,y=200)
# miLabel.place(x=100,y=200) #Es como un pack pero para un lugar específico
root.mainloop()

from tkinter import *
raiz = Tk()
miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()
miLabel = Label(miFrame, text="Hola alumnos de Python", fg="blue", font=("Comic Sans MS", 18))
miLabel.place(x=100, y=200)
miImagen = PhotoImage(file="nombreDeLaImagen.gif")
miLabel = Label(miFrame, image=miImagen)
miLabel.place(x=100, y=200)
raiz.mainloop()
