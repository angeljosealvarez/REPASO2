#MANEJO DE ARCHIVOS#
from io import open

archivo_texto=open("archivo.txt", "r+")

#w+ = se usa para escribir en un archivo y resetearlo
#r+ se usa para escribir en un archivo y que se empiece a escribir desde la pos del puntero (seek)

"""
archivo_texto.write("\n siempre es una buena ocasion para estudiar Python")
archivo_texto.close()
"""
lista_texto = archivo_texto.readlines()
lista_texto[2] = "Esta línea ha sido modificada"

archivo_texto.seek(len(archivo_texto.r))
texto= archivo_texto.read()
archivo_texto.seek(0) #Puntero del archivo, la barrita que aparece y desaparece al escribir
textoEnLista = archivo_texto.readlines() #lee la información línea a línea y la almacena en una lista
archivo_texto.writelines(textoEnLista)
print(texto)
archivo_texto.seek(0)
print(textoEnLista[0]) #Para que funcione hay que quitar el read ya que el cursor se sitúa al final luego de leer el texto una vez
contenido = texto
archivo_texto.seek(0)
mitad = round(len(contenido)/2)
print(archivo_texto.read(mitad))
archivo_texto.close()
#archivo_texto.seek(len(archivo_texto.read(0))/2)

