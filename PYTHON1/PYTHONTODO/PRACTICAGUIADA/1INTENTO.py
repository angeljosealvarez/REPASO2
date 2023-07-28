from tkinter import *
from tkinter import messagebox
import sqlite3

raiz = Tk()
raiz.title("Base de datos")
barraMenu = Menu(raiz)

raiz.config(menu=barraMenu, width=50, height=50)

def Salir():
    valor = messagebox.askokcancel("Salir", "Desea salir de la aplicacion?")
    if valor == True:
        raiz.destroy()


def Conectar():
    baseDatos = sqlite3.connect("baseDatos")
    cursor = baseDatos.cursor()
    try:
        cursor.execute('''CREATE TABLE baseDatos (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE VARCHAR(50),
    PASSWORD VARCHAR (50),
    APELLIDO VARCHAR(50),
    DIRECCION VARCHAR (50),
    COMENTARIOS VARCHAR (250)
    ) ''')
    except:
        messagebox.showerror("Error", "La base de datos ya ha sido creada")

def EliminarTodo():
    Valor1.set("")
    Valor2.set("")
    Valor3.set("")
    Valor4.set("")
    Valor5.set("")
    EntradaTexto6.delete(1.0,END)


menu2 = Menu(barraMenu, tearoff= 0)
menu2.add_command(label="Conectar", command=Conectar)
menu2.add_command(label="Salir", command=Salir)

menu3 = Menu(barraMenu, tearoff=0)
menu3.add_command(label="Eliminar todo", command=EliminarTodo)


barraMenu.add_cascade(label="BBDD", menu = menu2)
barraMenu.add_cascade(label="Eliminar", menu= menu3)
#--------------------------FRAME Y GUI
miFrame = Frame(raiz, width=500, height= 500)
miFrame.pack()

#--LABELS
LabelID = Label(miFrame, text="ID:")
LabelID.grid(row=1,column=0, padx=10, pady=10)

LabelNombre = Label(miFrame, text="Nombre:")
LabelNombre.grid(row=2,column=0, padx=10, pady=10)

LabelPassword = Label(miFrame, text="Password:")
LabelPassword.grid(row=3,column=0, padx=10, pady=10)

LabelApellido = Label(miFrame, text="Apellido:")
LabelApellido.grid(row=4,column=0, padx=10, pady=10)

LabelDireccion = Label(miFrame, text="Dirección:")
LabelDireccion.grid(row=5,column=0, padx=10, pady=10)

LabelComentarios = Label(miFrame, text="Comentarios:")
LabelComentarios.grid(row=6,column=0, padx=10, pady=10)
#--ENTRADAS

Valor1 = StringVar()
Valor2 = StringVar()
Valor3 = StringVar()
Valor4 = StringVar()
Valor5 = StringVar()
Valor6 = StringVar()

EntradaTexto1= Entry(miFrame)
EntradaTexto1.grid(row=1, column=2, padx= 10, pady= 10)
EntradaTexto1.config(textvariable=Valor1, show="?", justify="right", fg="black", bg="white")

EntradaTexto2= Entry(miFrame)
EntradaTexto2.grid(row=2, column=2, padx= 10, pady= 10)
EntradaTexto2.config(textvariable=Valor2)

EntradaTexto3= Entry(miFrame)
EntradaTexto3.grid(row=3, column=2, padx= 10, pady= 10)
EntradaTexto3.config(textvariable=Valor3)

EntradaTexto4= Entry(miFrame)
EntradaTexto4.grid(row=4, column=2, padx= 10, pady= 10)
EntradaTexto4.config(textvariable=Valor4)

EntradaTexto5= Entry(miFrame)
EntradaTexto5.grid(row=5, column=2, padx= 10, pady= 10)
EntradaTexto5.config(textvariable=Valor5)

EntradaTexto6= Text(miFrame)
EntradaTexto6.grid(row=6, column=2, padx= 10, pady= 10, columnspan=4)
EntradaTexto6.config(width=15, height=10)
#ENTRADA TEXTO 6 Y SCROLLBAR







nuevaScroll = Scrollbar(miFrame, command = EntradaTexto6.yview)
nuevaScroll.grid(row=6, column=4, sticky="nsew", pady=20, padx=20)
EntradaTexto6.config(yscrollcommand=nuevaScroll.set)


#--BOTONES


def funcBoton1():
    #CONECTAMOS CON LA BASE DE DATOS
    baseDatos = sqlite3.connect("baseDatos")
    cursor = baseDatos.cursor() 
    #CREAMOS VARIABLES
    
    def agregar_entrada():
        EntradaTexto6.get(1.0, END)

    Diccionario = [
    (Valor2.get()),
    (Valor3.get()),
    (Valor4.get()),
    (Valor5.get()),
    (EntradaTexto6.get(1.0, END)),
    ]
    baseDatos.execute("INSERT INTO baseDatos (NOMBRE, PASSWORD, APELLIDO, DIRECCION, COMENTARIOS) VALUES (?,?,?,?,?)", Diccionario)
    print(EntradaTexto6.get(1.0, END))
    baseDatos.commit()
    cursor.close()
    baseDatos.close()
    #AÑADIMOS LAS VARIABLES
    
def funcBoton2():
    baseDatos = sqlite3.connect("baseDatos")
    cursor = baseDatos.cursor()
    cursor.execute("SELECT * FROM baseDatos")
    datos = cursor.fetchall()
    elID = Valor1.get()
    diccionario = tuple(datos[int(elID) - 1])
    
    #INSERTAMOS LOS VALORES EN CADA UNO DE LOS ENTRY
    Valor2.set(diccionario[1])
    Valor3.set(diccionario[2])
    Valor4.set(diccionario[3])
    Valor5.set(diccionario[4])
    EntradaTexto6.delete(1.0, END)
    EntradaTexto6.insert(END, str(diccionario[5]))
    
    
def funcBoton3():
    baseDatos = sqlite3.connect("baseDatos")
    cursor = baseDatos.cursor()
    cursor.execute("SELECT * FROM baseDatos")
    datos = cursor.fetchall()
    v1 = Valor1.get()
    cadaDato = datos[int(Valor1.get()) -1] #A PARTIR DE AQUÍ TENEMOS UN DICCIONARIO CON TODOS LOS VALORES PEDIDOS
    
    diccionario = [
        Valor2.get(),
        Valor3.get(),
        Valor4.get(),
        Valor5.get(),
        EntradaTexto6.get(1.0,END),
        Valor1.get()
    ]

    cursor.execute("UPDATE baseDatos SET NOMBRE = ?, PASSWORD = ?, APELLIDO = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = ?",
    diccionario)
    baseDatos.commit()



def funcBoton4():
    conexion = sqlite3.connect("baseDatos")
    cursor = conexion.cursor()
    print(Valor1.get())
    cursor.execute("DELETE FROM baseDatos WHERE ID = ?", Valor1.get())
    conexion.commit()
    
    
    
    
   
    


Boton1 = Button(miFrame, text= "Create")
Boton1.grid(row=7, column=0, padx= 10, pady=10, columnspan=1)
Boton1.config(command=funcBoton1)


Boton2 = Button(miFrame, text="Read")
Boton2.grid(row=7, column=1,padx = 10, pady = 10, columnspan = 1 )
Boton2.config(command=funcBoton2)

Boton3 = Button(miFrame, text="Update")
Boton3.grid(row=7, column=3,padx= 10, pady=10, columnspan = 1 )
Boton3.config(command=funcBoton3)

Boton4 = Button(miFrame, text = "Delete")
Boton4.grid(row=7,column=4,padx= 10, pady= 10, columnspan= 1)
Boton4.config(command=funcBoton4)

#FUNCION DE MENU3


raiz.mainloop()