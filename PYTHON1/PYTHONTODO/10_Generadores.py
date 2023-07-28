##GENERADORES##
##YIELD##
"""
def generaPares(límite):

    num = 1
    milista = []

    while num <= límite - num: #Si tomamos como ejemplo num = 6 y límite = 12 no puede llegar a 7 porque = 7 <= 12 - 7 ; 7 <= 5

        milista.append(num*2)

        num += 1
    return milista

número_límite = int(input("Introduce un número: "))
"""

##CON GENERADOR YIELD
"""
#FORMA 2 SIN YIELD 
def generaPares(límite):

    num = 1
    milista = []

    while num <= límite - num: #Si tomamos como ejemplo num = 6 y límite = 12 no puede llegar a 7 porque = 7 <= 12 - 7 ; 7 <= 5

        milista.append(num*2)
        
        num += 1

    return milista

print(generaPares(10))

"""

##CON YIELD##


def generaPares(límite):

    num = 1
    

    while num <= límite - num: #Si tomamos como ejemplo num = 6 y límite = 12 no puede llegar a 7 porque = 7 <= 12 - 7 ; 7 <= 5

      yield num*2

      num += 1

   

print(next(generaPares(10))) #Retorna el siguiente elemento de un objeto iterable (Permite almacenar valores uno a uno sin tener que almacener la lista entera consumiendo así más memoria)

for n in generaPares(10):
   print(n)
