class Persona():
    def __init__(self, nombre, edad, lugar_de_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_de_residencia = lugar_de_residencia
    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nLugar de residencia:", self.lugar_de_residencia)
class Empleado(Persona): #Una subclase es siempre una superclase, ya que un empleado es siempre una persona
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad
    def descripcion(self):
        super().descripcion()
        print("\nSalario: ", self.salario, "\nAntigüedad: ", self.antigüedad, "\nLugar de residencia del empleado: ", self.lugar_de_residencia)
Antonio = Empleado(1500, 15, "Alfredo", 20, "España")
Antonio.descripcion()
print(isinstance(Antonio, Empleado))

Nombre = Empleado()