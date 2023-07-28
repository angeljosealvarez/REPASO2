#CREACIÓN DE VENTANAS GRÁFICAS

#Ventanas emergentes. Abrir archivos

from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", filetypes= (("Archivos de texto2", "*.txt"), ("Archivos de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)

Button(raiz, text="Abrir fichero", command=abreFichero).pack()

raiz.mainloop()


"""
VERSIÓN REDUCIDA

from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Textos", "*.txt"), ("Todos los ficheros", "*.*")))

Button(raiz, text="Abrir fichero", command= abreFichero).pack()
raiz.mainloop()



OPCION PARA COMPROBAR 

def CerrarAplicacion():
    valor = messagebox.askretrycancel("Desea reintentar antes de salir")
    if valor == False:
        raiz.destroy()
    else:
        label = Label(raiz , text="Hola que tal").pack()

"""