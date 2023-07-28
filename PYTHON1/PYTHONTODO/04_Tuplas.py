## TUPLAS ##

#Las tuplas no se pueden cambiar
#Permiten extraer porciones
#No permiten hacer busquedas (index)
#Si permiten comprobar si un elemento está en una tupla

miTupla = ("Esto", "Es", "Una", "Tupla")
miLista = list(miTupla) #Convertir una Tupla a lista
miLista.remove("Tupla")
miLista.append("Lista")

print(miLista)
print(miTupla)

print(miTupla.count("Es")) #Saber cuantas veces se repite un elemento

print(len(miTupla)) #Te dice el número de elementos que hay en una Tupla

#Añadir a cada elemento de una tupla una variable (desempaquetado de tuplas)

tupla = ("tupla", "tupla2", "tupla3")
tupla1, tupla2, tupla3 = tupla
print(tupla1)
