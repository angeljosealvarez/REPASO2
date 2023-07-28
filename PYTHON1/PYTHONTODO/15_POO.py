##INTRODUCCIÓN DE POO##

# Poo (programación orientada a objetos) se encargan de trasladar la naturaleza de un objeto hacia el código de programación, este objeto tiene un estado de movimiento, tiene unas propiedades específicas y un comportamiento específico
# Las ventajas de POO son que el código estará dividido en trozos, en partes, módulos, clases, también conocido como Modularización
# Es muy reutilizable
# Si existe algún fallo el código se seguirá ejecutando, a lo que llamamos excepciones
# Encapsulamiento

# Reutilizar un código se denomina "Herencia"


"""VOCABULARIO POO

CLASE: modelo de objeto donde se redactan las características comunes de un grupo de objetos (como las ruedas de un coche, que se comparte en otros coches, la clase sería las ruedas y el coche los objetos a usar)
EJEMPLAR, INSTANCIA, OBJETO DE CLASE: instancia es objeto ejemplar de una clase
MODULARIZACIÓN: conjunto de clases que pueden ser reutilizables (utilizar trozos de un programa en otros)
ENCAPSULACIÓN: proteger una clase para que niguna otra clase puede saber nada de ella, aunque todas las clases estén conectadas desde el mismo equipo (imaginar equipo de sonido)
MÉTODOS DE ACCESO: métodos para que las diferentes clases se conecten unas a otras
NOMENCLATURA DEL PUNTO: la nomenclatura del punto se usa para acceder a descripciones específicas, se pueden acceder a propiedades del objeto y el comportamiento del objeto"""


class Coche():
    def __init__(self):
        # Estado inicial de la clase, es un método constructor para que al añadir un objeto por defecto ya tenga las propiedades
        # PROPIEDADES
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4 #Encapsular una propiedad para que no pueda ser modificada a la hora de crear un nuevo objeto
        self.enmarcha = False
        
    # COMPORTAMIENTO
    # En el comportamiento se añaden métodos, que son funciones especiales que se añaden a las clases, mientras que una función no pertenece a ninguna clase
    def arrancar(self, arrancamos):
        # self solo es el objeto del que estamos a hablar, en este caso es miCoche
        self.enmarcha = arrancamos
        if self.enmarcha:
            print("El coche está en marcha")
        else:
            print("El coche está parado")

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Largo chasis:", self.largoChasis, "cm, Ancho chasis:", self.anchoChasis, "cm. Estado de marcha:", self.enmarcha)

    def chequeo_interno(self):
        print("Realizando chequeo interno")
        if self.enmarcha:
            self.gasolina = "ok"
            self.aceite = "ok"
            self.puertas = "cerradas"
            if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
             return True 
            else:
                return False
        chequeo = self.chequeo_interno
        if self.enmarcha and chequeo:
            return "El coche está en marcha"
        elif self.enmarcha and chequeo == False:
            print("El chequeo no ha funcionado correctamente")
        else:
            print("No está en marcha el coche o ocurrieron 2 fallos")



miCoche = Coche()  # Instanciar una clase (añadir una instancia a una clase)
print(miCoche.largoChasis)
miCoche.arrancar(True)
miCoche.estado()

# A continuación creamos el segundo objeto
print("\nA continuación creamos el segundo objeto")
miCoche2 = Coche()
miCoche2.chequeo_interno()
miCoche2.arrancar(False)
miCoche2.__ruedas = 2  #Shadowing (crear una propiedad que tiene el mismo nombre que cualquiera otra propiedad mencionada anteriormente (esto no estaba dentro del contenido del video de youtube))
print(miCoche2.__ruedas) #Se puede cambiar desde fuera pero no se puede cambiar una función integrada ya en la clase
miCoche2.estado()

   


    
    
