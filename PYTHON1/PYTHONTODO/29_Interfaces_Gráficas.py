#INTERFACES GRÁFICAS CALCULADORA
from tkinter import *
raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

operación = "" #Las variables global sirve para modificarlas ya sea dentro de funciones, clases, ¿listas?...
resultado = 0

#PANTALLA-----------------------------------------------------------------------------------------------

númeroPantalla = StringVar()

pantalla=Entry(miFrame, textvariable=númeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #columnspan indica cuantas columnas ocupa
pantalla.config(background="black", fg="#03f943", justify="right")

#PULSACIONES TECLADO---------------------------------------------------------------------------------------

def númeroPulsado(num):

    global operación

    if operación !="":
        númeroPantalla.set(num)
        operación = ""
    elif operación == "suma":
        númeroPantalla.set(númeroPantalla.get())
    else:
        númeroPantalla.set(númeroPantalla.get() + num)
   

    

#FUNCIÓN SUMA--------------------------------------------------------------------------------------------

def suma(num):
    global operación
    global resultado

    resultado += int(num)
    operación="suma"
    númeroPantalla.set(resultado)

#FUNCIÓN RESULTADO-----------------------------------------------------------------------------------------

def el_resultado():
    global resultado
    númeroPantalla.set(resultado+int(númeroPantalla.get()))
    resultado = 0


#FILA1-----------------------------------------------------------------------------------------------

boton7 = Button(miFrame, text="7", width=3, command=lambda:númeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda:númeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda:númeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)

#FILA2-------------------------------------------------------------------

boton4 = Button(miFrame, text="4", width=3, command=lambda:númeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda:númeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda:númeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="*", width=3)
botonMult.grid(row=3, column=4)


#FILA3-----------------------------------------------------------------------------------------------

boton1 = Button(miFrame, text="1", width=3, command=lambda:númeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda:númeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda:númeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest = Button(miFrame, text="-", width=3)
botonRest.grid(row=4, column=4)

#FILA4-----------------------------------------------------------------------------------------------

boton0= Button(miFrame, text="0", width=3, command=lambda:númeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda:númeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda:suma(númeroPantalla.get()))
botonIgual.grid(row=5, column=3)
botonSuma = Button(miFrame, text="+", width=3, command=lambda:suma(númeroPantalla.get()))
botonSuma.grid(row=5, column=4)

#SIGUIENTE VIDEO DE INTERFACES





raiz.mainloop()