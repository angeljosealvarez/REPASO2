
"""
nombreUsuario = input("Introduce tu nombre de usuario: ")
print("Tu nombre es: ", nombreUsuario.upper(), nombreUsuario.lower(), nombreUsuario.capitalize())
edad = input("Introduce tu edad: ")
while edad.isdigit() == False:
    print("Por favor, introduce un valor numérico")
    edad = input("Introduce tu edad: ")
if int(edad)< 18:
    print("No puedes pasar")
else:
    print("Puedes pasar")
print(edad.isdigit())
"""

email = input("Introduce un email: ")
arroba = email.count("@")
print(email.rfind("@")) #Devuelve la última posición del valor que se pide
print(email.find("@"))
print(email[-1])
if email.rfind("@")!= 0 and email.rfind("@") != len(email)-1: #Se le añade -1 porque python empieza a contar desde 0
    print("No hay arroba ni al principio ni al final")
if arroba >= 1 or email.rfind("@")== 0 or -1 == False:
    print("Email correcto")