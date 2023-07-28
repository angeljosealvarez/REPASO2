#WIDGET BUTTON Y TEXTO
"""
Los widget button son botones para interactuar con la interfaz
"""

from tkinter import *

#FRAME Y RAÍZ

raiz = Tk()
miFrame = Frame(raiz, width=500, height=500)
miFrame.pack()

#CUADROS
miNombre=StringVar() #Con esta clase le decimos a la variable que se trata de una cadena de caracteres

cuadroTexto = Entry(miFrame,textvariable=miNombre)
cuadroTexto.grid(row=1, column=2)

cuadroContraseña = Entry(miFrame)
cuadroContraseña.grid(row=4, column=2)
cuadroContraseña.config(fg="blue", justify="center", show="*") #CAMBIAR COLOR CON FG Y LA ALINEACIÓN DEL TEXTO CON JUSTIFY

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=2)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=2,)

#TEXTOS

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=2, padx=10, pady=10) #CUANDO LLEGA AL FINAL TIENE SCROLL PERO HAY QUE AGREGARLO DE MANERA MANUAL

#SCROLL

scrollVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrollVertical.grid(row=5, column=3, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVertical.set)


#LABELS

nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=1, sticky="w", pady=10, padx=10)

direccionLabel = Label(miFrame, text="Dirección: ")
direccionLabel.grid(row=3, column=1, sticky="w", pady=10, padx=10)

apellidoLabel = Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=1, sticky="w", pady=10, padx=10)

contraseñaLabel = Label(miFrame, text="Contraseña: ")
contraseñaLabel.grid(row=4, column=1, sticky="w", pady=10, padx=10)

comentariosLabel = Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=1, sticky="w", pady=10, padx=10)

#BOTONES
def codigoBoton():
    miNombre.set("Ángel") #Establecer un valor a una variable con la StringVar
botonEnvio = Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()   

raiz.mainloop()

