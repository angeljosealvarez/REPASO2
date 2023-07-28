##EXCEPCIONES##
"""
def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        return ("Eres muy joven")
        
print(evaluaEdad(-1))
"""

#La función raise en Python se utiliza para lanzar explícitamente una excepción en un momento determinado del programa, en lugar de esperar a que ocurra un error en tiempo de ejecución
import math

def CalcularRaiz(num1):

    if num1 < 0:
        raise ValueError ("El número no puede ser negativo")
    
    else:
        raízCuadrada = math.sqrt(num1)
   
        return raízCuadrada
    

    

    


    
    
try:

    print(int(CalcularRaiz(-4)))

except ValueError as errorNúmeroNegativo:
    print(errorNúmeroNegativo)