#WIDGET MENÚ

#CREACIÓN DE BARRAS DE MENÚ

from tkinter import *

raiz = Tk()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdición = Menu(barraMenu, tearoff= 0)
archivoEdición.add_command(label="Copiar")
archivoEdición.add_command(label="Cortar")
archivoEdición.add_command(label="Pegar")


archivoHerramientas = Menu(barraMenu, tearoff= 0)
archivoAyuda = Menu(barraMenu, tearoff= 0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdición)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

raiz.mainloop()

"""
VERSION REDUCIDA

from tkinter import *
raiz = Tk()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width= 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff= 0)
archivoMenu.add_command(label="Nuevo")

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

raiz.mainloop()
"""