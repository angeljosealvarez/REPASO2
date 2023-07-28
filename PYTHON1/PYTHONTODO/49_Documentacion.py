#https://www.youtube.com/watch?v=SJqANWdRG4I
#DOCUMENTACION
def areaCuadrado(num1,num2):
    """Calculamos el área de un cuadrado
    usando base por altura"""
    return num1*num2
print(areaCuadrado.__doc__)
#help(areaCuadrado) #ofrece más datos

import doctest

def areaCuadrado(num1, num2):
    """Calculamos el área de un cuadrado
    usando base por altura y dividiendolo entre 2
    >>> areaCuadrado(2,3)
    3.0"""
    return (num1*num2) / 2
print(areaCuadrado.__doc__)
print(areaCuadrado(2,3))
doctest.testmod()