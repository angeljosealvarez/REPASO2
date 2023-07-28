##EXCEPCIONES##

def divide():
    
    try:
        op1 = float(input("Introduce un número: "))
        op2 = float(input("Introduce otro número: "))

        print("La división es: " + str(op1/op2))
        print("Cálculo finalizado")

    except ValueError:

        print("El valor introducido es erróneo")

    except ZeroDivisionError:

        print("No se puede dividir entre cero")

    finally: #Que el código se ejecute siempre haya error o no

        print("HolaHolaHolaHola")




divide()

print("Cálculo finalizado")