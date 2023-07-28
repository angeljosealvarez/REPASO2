#SERIALIZACION#

"""
La serialización consiste transportar el código creado en una base de datos, a través de la biblioteca "import pickle" en la cual podemos:
cargar los datos que tengamos ya previamente en el código, un ejemplo es una clase, se usa con load()
agregar datos en el fichero previamente creado con la función dump()

"""
"""
import pickle

lista_nombres = ["María", "Juan", "Pedro"]
fichero_binario = open("lista_nombres2","wb")
#VOLCAMOS INFORMACIÓN
pickle.dump(lista_nombres, fichero_binario) #Toma dos argumentos, el primero es el fichero que queremos volcar, y el segundo es al archivo o fichero que ya tenemos guardado en el disco duro
fichero_binario.close()
del fichero_binario
"""
import pickle

fichero = open("lista_nombres2", "rb")
lista = pickle.load(fichero)
print(lista)