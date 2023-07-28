#https://www.youtube.com/watch?v=4dkjpHI6vpA&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=68
#FUNCION MAP
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)



listaEmpleados = [

Empleado("Juan", "Director", 6700),
Empleado("Ana", "Presidenta", 7500),
Empleado("Antonio", "Administrativo", 2100),
Empleado("Sara", "Secretaria", 2150),
Empleado("Mario", "Botones", 1800),

]

def calculoComision(empleado):
    if (empleado.salario<=3000):
        empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleadosComision=map(calculoComision, listaEmpleados)
for empleado in listaEmpleadosComision:
    print(empleado) 