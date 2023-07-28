

from tkinter import *
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

operación = 0
número = ""



númeroPantalla = StringVar()
def Function(num):
    global operación
    global número
    
    if número == "+":
        númeroPantalla.set(num)
        número = ""
    else: 
        númeroPantalla.set(númeroPantalla.get() + num)
        print(númeroPantalla.get())


def Function1(signo):
    global operación
    global número
    if signo == "+":
        número = "+"
        operación += int(númeroPantalla.get())
        print(operación)
        númeroPantalla.set(operación)
    
    elif signo == "=":
        operación += int(númeroPantalla.get())
        númeroPantalla.set(operación)







entradaTeclado = Entry(miFrame, textvariable=númeroPantalla)
entradaTeclado.grid(row=1, column=0, columnspan= 4)

boton = Button(miFrame, text="1", command=lambda:Function("1"))
boton.grid(row=0, column=0)

boton = Button(miFrame, text="+", command=lambda:Function1("+"))
boton.grid(row=0, column=1)


boton = Button(miFrame, text="=", command=lambda:Function1("="))
boton.grid(row=0, column=2)


raiz.mainloop()



"""
from tkinter import *
raiz = Tk()
miFrame = Frame(raiz)
miFrame.pack()

entradaTexto = StringVar()

def buttonText():
    entradaTexto.set("Hola")
    print(entradaTexto.get())

Boton = Button(miFrame, text="Click me", command=lambda:buttonText())
Boton.pack()

raiz.mainloop()

"""