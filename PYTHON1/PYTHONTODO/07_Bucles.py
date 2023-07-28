for i in [1,2,3]: #No detecta los números enteros como valores a repetir, sino el número de elementos que hay en la lista
    print("Hola")
    print(i)
    print("Ese es el valor de i")

print("\n")

for i in ["Prueba", "Bucle", "Para", "Informática"]:
    print("Hola", end="   ")    

for i in "tantoscaracterestengaestestring":
    print("Hola", end=" ")    

##DETECTAR SI HAY UN EMAIL##

"""


email = 0
miemail = input("Introduce tu email:")


for i in miemail:
    if miemail.count("@") > 1:
        print("Email no es correcto por arroba")
    elif miemail.count(".") > 1:
        print("Email no es correcto por punto")
    elif miemail == "@" or ".":
        email = email + 1
  

if email == 2:
    print("hay un email")   
else:
    print("El email es incorrecto")

"""
for i in range(5,10,3): #Comienza en, Termina en, Saltos que da
    print(f"valor de la variable {i}")

valido = False
email = input("Introduce un email: ")

for i in range(len(email)):

    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")