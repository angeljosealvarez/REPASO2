#https://www.youtube.com/watch?v=qpwn3gRtxCo&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=69
#SIRVEN PARA BUSCAR ALGÚN DETALLE ESPECÍFICO EN UNA CADENA DE TEXTO O VALOR IMPORTANTE

import re
cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoBuscar2 = "Python"
textoBuscar = "aprender"
textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start()) #Donde comienza el texto
print(textoEncontrado.end()) #Donde termina el texto
print(textoEncontrado.span()) #Hace las dos cosas y las devuelve en una tupla
print(len(re.findall(textoBuscar2, cadena))) #Findall devuelve una lista de cuantos python hay y usamos len para que devuelva la longitud de la lista, en este caso 2

#https://www.youtube.com/watch?v=V8316ao08tQ
#METACARACTERES Y ANCLAS

'''El metacaracter ^ en la biblioteca re de Python se utiliza para buscar una cadena de texto que comience con un patrón específico.
ESTOS DOS METACARÁCTERES NOS PUEDEN SERVIR PARA BUSCAR DOMINIOS DE PÁGINAS WEB (.COM, .ES...)'''
lista_nombres=['Ana Gómez', 'María Martín', 'Sandra López', 'Santiago Martín']
for i in lista_nombres:
    if re.findall('^Sandra', i): #El metacaracter ^ buscará que nombre en la lista comienza por Sandra. Devolviendo el nombre completo
        print(i)

for i in lista_nombres:
    if re.findall('López$', i): #El metacaracter $ buscará que cadena de texto finaliza con López
        print(i)

for i in lista_nombres:
    if re.findall('[A]', i): #El metacaracter $ buscará que cadena de texto finaliza con López
        print(i)