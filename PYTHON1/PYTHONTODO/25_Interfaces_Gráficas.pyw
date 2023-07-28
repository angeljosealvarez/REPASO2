#El uso de pyw se usa para que no salga la consola de python al abrir el archivo fuera de Visual Studio Code
#Pack se usa para que un añadir o integrar un frame, widget o raiz dentro de la propia raiz, widget o frame
"""
FRAMES

miFrame = Frame(contenedor, width=x, height=y) en valor int

ANCLADO: miFrame.pack(side="right", anchor"n") n de north, s de south...
RELLENADO: miFrame.pack(fill="x")
para que haga fill en y tendría que ser: miFrame.pack(fill="y", expand=True)
BORDE: miFrame.config(bd=20) and miFrame.config(relief="groove")
CURSOR: miFrame.config(cursor="hand2")

CURSOR Y BORDE SE PUEDE APLICAR A LA RAIZ
"""
from tkinter import *
raiz= Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1,1) #o raiz.resizable(True,False) #Se puede aumentar o disminuir el tamaño de la interfaz co raiz.resizable suponiendo que rais = Tk()
raiz.iconbitmap("CAMISETA DE OSO.ico")
#No se necesita geometry debido que al usar un frame y ejecutar el programa este establece su tamaño al tamaño que tiene por defecto el frame con miFrame.config(width="650", height="350")
raiz.geometry("650x350") #no confundamos geometry con resizable, resizable establece por defecto mientras que geometry es encargado de establecer el tamaño al acceder a la interfaz por defecto
raiz.config(bg="blue")
raiz.config(bd=20) #añadir borde modificando su tamaño
raiz.config(relief="groove")
raiz.config(cursor="hand2")
miFrame= Frame()
miFrame.pack()
miFrame.config(bg= "red")
miFrame.config(width="650",  height="200")
miFrame.pack(side="right")              #side= "right", anchor="n" #ANCHOR ES PARA QUE SE ESTABLEZCA EN LA PARTE SUPERIOR DE LA ESQUINA DERECHA
miFrame.pack(fill= Y, expand="True")
#miFrame.pack(fill="x")
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(cursor="hand2")
raiz.mainloop()
