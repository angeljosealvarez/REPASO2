def areaCuadrado(num1):
    """Para calcular el área multiplicamos la base por su altura, o lo que es lo mismo, lado elevado al cuadrado
    >>> areaCuadrado(2)
    4"""
    return num1*num1
print(areaCuadrado(4))

help(areaCuadrado)

def email(usuario):

    """Aquí se podría usar eficientemente la documentación de la siguiente manera: 
    >>> email("Carlos@gmail.com")
    True
    >>> email("Carlos@gmail.com@")
    False"""
    arroba = usuario.count("@")
    if (arroba !=1 or usuario.rfind("@")==(len(usuario)-1)or usuario.rfind("@")==0):
        return False
    else:
        return True
print(email("Carlos@gmail.com"))
import doctest #RECORDAR QUE PUEDE SER UN NÚMERO FLOAT (4.0 EN VEZ DE 4)
doctest.testmod()


#DOCUMENTACION CLASE 3
import math
def raiz(numero):

    """
    >>> lista = []
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raiz(lista)
    [2.0, 3.0, 4.0]

    
    >>> lista = []
    >>> for i in [4,-9,16]:
    ...     lista.append(i)
    >>> raiz(lista)
    Traceback (most recent call last):
        ... 
    ValueError: math domain error
        
    """   
    return [math.sqrt(n) for n in numero]


doctest.testmod()