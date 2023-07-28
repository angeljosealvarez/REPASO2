area_triangulo = lambda b,h:(b*h)/2
print(area_triangulo(5,7))

destacar_valor = lambda comision:"¡{}!$".format(comision)
ana_comision = 20000005000000000
print(destacar_valor(ana_comision))

numeros = [20,30,40,51,53,55,40,302,12312,1023,120310,2349,48254,3485]
print(list(filter(lambda num:num % 2 == 0, numeros)))

class Empleado():
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.cargo,self.salario)
    
listaEmpleados = [

    Empleado("Juan", "Director", 750000),
    Empleado("Ana", "Presidenta", 85000),
    Empleado("Antonio", "Administrativo", 25000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000),
]

salarios_altos = filter(lambda empleado:empleado.salario > 80000,listaEmpleados)
for empleado in salarios_altos:
    print(empleado)

def CalculoComision(empleado):
    if empleado.salario > 80000:
        empleado.salario = empleado.salario *1.03
    return empleado

listaEmpleadosComision = map(CalculoComision, listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado)