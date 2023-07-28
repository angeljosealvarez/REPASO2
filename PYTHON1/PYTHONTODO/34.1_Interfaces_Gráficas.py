from tkinter import *
from tkinter import filedialog

raiz = Tk()

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Texto", "*.txt"), ("Todos los tipos de archivo", "*.*")))
    print(fichero)



Button(raiz, text="Abrir fichero", command=abreFichero).pack()

raiz.mainloop()