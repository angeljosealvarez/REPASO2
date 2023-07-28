import re

cadena = ['Ana', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']
for elemento in cadena:
    '''si a [o-t] se le añade un metacaracter cualquiera, ya sea $ por poner un ejemplo, este buscará cualquier palabra que tenga como carácter final una letra
    del abecedario que este entre la o y la t'''
    if re.findall('[^o-t]', elemento): #Busca aquellas palabras que tengan un rango de letras comprendidos entre la o y la t
        print(elemento)