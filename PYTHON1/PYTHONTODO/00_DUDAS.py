class Persona:
    def __init__(self, nombre, apellidos, lugar_de_residencia):
        self.nombre = nombre
        self.apellidos = apellidos
        self.lugar_de_residencia = lugar_de_residencia

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.apellidos, self.lugar_de_residencia)

persona = Persona("Angel", "Jose", "Casa")
print(persona)