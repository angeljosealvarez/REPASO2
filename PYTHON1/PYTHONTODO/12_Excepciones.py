##EXCEPCIONES##







def división(num1, num2):
    
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Hay un error con el valor, al parecer añadistes algún valor en la división que era un cero")
        return("Operación errónea")
    
while True:
    try: 
        numero1 = (int(input("Introduce dos números a dividir: ")))
        numero2 = (int(input("Introduce dos números a dividir: ")))  
        break
    except ValueError:
        print("Los valores introducidos no son correctos")


    

print(numero1)
print(numero2)

print(división(numero1,numero2))

print("El programa se sigue ejecutando")


