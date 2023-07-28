#WIDGET BUTTON Y TEXTO
"""para orientar la scrollbar hacia la dirección que nosotros queramos se usa yview
para hacer que se adapte al texto que hay en la interfaz se usa nsew"""
from tkinter import *

#FRAME Y RAÍZ

raiz = Tk()
miFrame = Frame(raiz, width=500, height=500)
miFrame.pack()

miNombre = StringVar() #Cadena de carácteres
#TEXTO

textoComentario = Text(miFrame, width=10, height=5)
textoComentario.grid(row=2, column=2, padx=10, pady=10)

#SCROLL

scrollVert = Scrollbar(miFrame, command=textoComentario.yview) 
scrollVert.grid(row=2,column=3, sticky="nsew" )
textoComentario.config(yscrollcommand=scrollVert.set)


#CUADRO

cuadroTexto = Entry(miFrame, textvariable=miNombre) #Hace que se asocie miNombre = StringVar()
cuadroTexto.grid(row=1, column=2, sticky="w", pady=10, padx=10)

#LABEL

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=1, column=1, sticky="w", pady=10, padx=10)

#BOTÓN
def códigoBotón():
    
    miNombre.set("Ángel")
botón = Button(raiz, text="Enviar", command=códigoBotón)
botón.pack()
#CUANDO ESTÁ EN RAIZ SE DEBE HACER .PACK





raiz.mainloop()