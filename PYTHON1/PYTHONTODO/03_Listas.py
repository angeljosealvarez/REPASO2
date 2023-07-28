## LISTAS ##
miLista = ["María", "Pepe", "Marta", "Manolo"]


print(miLista[:]) #Imprimir lista completa

print("\n")

print(miLista[2]) #Acceder a un índice concreto
print(miLista[-2]) #Acceder a un índice concreto

print("\n")

print(miLista[0:3]) #Acceder desde un índice x hasta un índice y
print(miLista[:3]) #Acceder desde un índice x hasta un índice y

print("\n")

print(miLista[2:]) #Acceder desde un elemento hasta el final

print("\n")

miLista.append("Sandra") #Añadir elemento al final de una lista
print(miLista[:])

print("\n")

miLista.insert(2, "Manola") #Añadir elemento desde un índice que nosotros añadamos
print(miLista)

print("\n")

miLista.extend(["Ángel", "Juan", "José"]) #Añadir los elementos de la lista más los que se añadieron actualmente
print(miLista)

print("\n")

print(miLista.index("Ángel")) #Te dice el índice en el que esta un elemento

print("\n")

print("Pepe" in miLista) #Imprime una valor boolean afirmando o no si un elemento se encuentra en la lista

print("\n")

miLista.remove("Pepe") #Eliminar un elemento de una lista
print(miLista)

print("\n")

miLista.pop() #Elimina el último elemento de una lista


#Sumar listas:
miLista2 = ["Hola", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
miLista3 = ["Hola2", 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(miLista2 + miLista3)

print("\n")

#Multiplicar listas
print(miLista2*3)