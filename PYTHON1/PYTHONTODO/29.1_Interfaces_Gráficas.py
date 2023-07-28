from tkinter import *
raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()

#PULSACIONES TECLADO

def númeroPulsado(num):

    númeroPantalla.set(númeroPantalla.get()+ num)


#PANTALLA

númeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=númeroPantalla)
pantalla.grid(row=1, column=1, padx= 10, pady= 10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#FILA 1

boton7 = Button(miFrame, text="7", width=3, command=lambda:númeroPulsado("7"))












raiz.mainloop()