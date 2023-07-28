#https://www.youtube.com/watch?v=DQXm6bIZgvk
#DECORADORES
#
def funcion_decoradora(funcion): #La funcion decoradora se encarga de DECORAR, es decir, solo se encarga de activarse cuando hay @
    
    def funcion_interior(*args, **kwargs): #La funcion interior realiza el codigo ya establecido por python, la funcion decoradora en cambio está limitada a activarse en una funcion normal
        #kwargs se refiere a argumentos con clave, como un diccionario
        print("Vamos a realizar un cálculo: ")
        print(funcion(*args, **kwargs))
        print("Hemos terminado el cálculo")
    return funcion_interior


@funcion_decoradora
def suma(num1,num2, num3):
    return num1 + num2 + num3
@funcion_decoradora
def resta(num1, num2):
    return num1 - num2

@funcion_decoradora
def potencia(base, exponente):
    return pow(base, exponente)



resta(7,5)
suma(12,10,8)
potencia(base = 5, exponente =3)