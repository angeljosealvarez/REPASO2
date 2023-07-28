#https://www.youtube.com/watch?v=u3WBRgpxQcc
#MATCH Y SEARCH

import re
nombre1 = 'Jara López'
nombre2 = '43954395'
nombre3 = 'Lara López'
'''
if re.match("Sandra", nombre2, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")
'''
if re.search("López", nombre1, re.IGNORECASE): #Busca las cadenas de texto que comienzan por cualquiera y a continuación ara #SEARCH BUSCA DESDE CUALQUIER PUNTO
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")