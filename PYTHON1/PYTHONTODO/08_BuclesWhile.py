i = 1


while i <= 10:
    print("Ejecución " + str(i))
    i = i+1

print("Terminó la ejecución")


edad = int(input("Introduce tu edad por favor: "))

while edad < 5 or edad > 100:
    print("Introduce una edad correcta por favor")
    edad = int(input("Introduce tu edad por favor"))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))


print("Programa de cálculo de raíz cuadrada")
numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
    print("El número es negativo")

    intentos = intentos + 1
    print(intentos)
    if intentos >= 2:
        print("No tienes más intentos")
        break;
    numero = int(input("Introduce un número por favor: "))
    

if numero > 0:
    solución = numero + 1
    print("La solución es " + str(solución))



       

