def funcion_decoradora(funcion): #La funcion decoradora se encarga de DECORAR, es decir, solo se encarga de activarse cuando hay @
    
    def funcion_interior(): #La funcion interior realiza el codigo ya establecido por python, la funcion decoradora en cambio está limitada a activarse en una funcion normal
        print("Vamos a realizar un cálculo: ")
        funcion()
        print("Hemos terminado el cálculo")
    return funcion_interior








def suma(num1,num2):
    print(num1+num2)
@funcion_decoradora
def resta():
    print(30-10)
resta()
