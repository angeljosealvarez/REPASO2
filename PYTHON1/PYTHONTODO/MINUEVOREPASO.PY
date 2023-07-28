from io import open
archivo_texto = open("MYNEWTEXTFILE.txt", "r+")
#r+ escribir desde la posicion del fichero que hayamos indicado
#w+ escribir en un fichero y resetearlo

archivo_texto.write("Hola mundo")
texto = archivo_texto.read()
archivo_texto.seek(0)
textoEnLista = archivo_texto.readlines()
archivo_texto.writelines(textoEnLista)
print(texto)
contenido = texto
mitad = round(len(contenido)/2)
archivo_texto.close()