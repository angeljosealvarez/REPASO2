##DICCIONARIOS##

#Clave:valor

miDiccionario = {"Diccionario": "significado",
                 "Diccionario2": "significado2"}

print(miDiccionario["Diccionario"])

miDiccionario["Diccionario"] = "Lisboa" #Cambiar el valor de un elemento por otro
print(miDiccionario)

del miDiccionario["Diccionario"] #Eliminar una clave y valor de un diccionario añadiendo solo la clave
print(miDiccionario)

print(miDiccionario.keys()) #Imprime las claves que existen en un diccionario
print(miDiccionario.values()) #Imprime los valores que existen en un diccionario
print(len(miDiccionario)) #Imprime cuantas Clave:Valor existen en un diccionario