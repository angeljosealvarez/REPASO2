#LAMBDA
area_triangulo = lambda b,h:(b*h)/2
print(area_triangulo(2,3))
#---
empleo = lambda dinero:"¡{}$!".format(dinero)
print(empleo(20000500000))
#FILTER
'''Trabaja con valores que son True o False'''
class SueldoPersona():
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self): #STR sirve para que al llamar una clase devuelva junto con la clase la cadena de texto que nosotors hayamos pasado
        return "{} tiene un sueldo de {}".format(self.nombre, self.sueldo)
listaPersonas = [SueldoPersona("Carlos", 60000),
                 SueldoPersona("Alguien", 30000)]
personas = filter(lambda empleado:empleado.sueldo > 50000, listaPersonas)
for empleado in personas:
    print(empleado)
#MAP
"""funciona como filtrer pero admite funciones que no son lambda (más complejas)"""
#HACEMOS LA CLASE
class Persona():
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self):
        return "{} tiene un sueldo de {}".format(self.nombre,self.sueldo)
#HACEMOS LA FUNCON
def masComplejo(persona):
    if persona.sueldo > 50000:
        print("Tienes un sueldo elevado")
    elif persona.sueldo <= 50000 :
        return "Tienes un sueldo no elevado"
Diccionario = [
    Persona("Carlos", 50001),
    Persona("Carlos2", 59999)
]
#USAMOS LA FUNCION MAP
esMap = map(masComplejo,Diccionario )
for persona in esMap:
    print(persona)

#EXPRESIONES REGULARES
import re
cadena = "Vamos a aprender expresiones regulares"
textoBuscar = "aprender"
textoBuscar2 = "expresiones"
textoEncontrado = re.search(textoBuscar,cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
print(re.findall(textoBuscar,cadena))

#METACARACTER
listaNombres = ["Un Carlos", "Juan", "Pedro", "Pepe"]
for i in listaNombres:
    print(re.findall("Carlos$", i))
    print(re.findall("[o]",i))