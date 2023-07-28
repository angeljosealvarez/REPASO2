class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
class Camión():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
def desplazamientoVehículo(vehículo): #Utilizar una clase para usarla en una función para que a través de diferentes clases una variable pueda cambiar de forma con la función
    vehículo.desplazamiento()
miVehículo = Coche() #Cambiar esto
miVehículo.desplazamiento()
desplazamientoVehículo(miVehículo)

#POLIMORFISMO ES USAR VARIAS CLASES PARA LUEGO CRAR UNA FUNCIÓN CUYO PARÁMETRO PRINCIPAL CORRESPONDA A LA VARIABLE CON VALORES DE UNA CLASE