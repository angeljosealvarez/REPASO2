#VENTANAS EMERGENTES

#Ventanas para informar, avisar o permitir realizar tareas al usuario

from tkinter import *
from tkinter import messagebox

raiz = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Ángel", "Procesador de textos versión 2023")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")
    if valor ==True: #asokcancel usa True or False mientras que askquestion usa "yes" o "no"
        raiz.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento bloqueado")
    if valor ==False:
        raiz.destroy()

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar DOCUMENTO", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdición = Menu(barraMenu, tearoff= 0)
archivoEdición.add_command(label="Copiar")
archivoEdición.add_command(label="Cortar")
archivoEdición.add_command(label="Pegar")


archivoHerramientas = Menu(barraMenu, tearoff= 0)
archivoAyuda = Menu(barraMenu, tearoff= 0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdición)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

raiz.mainloop()