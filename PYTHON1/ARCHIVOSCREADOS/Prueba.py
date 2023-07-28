import pickle
class Persona():
    def __init__(self, nombre, género, edad):
        self.nombre= nombre
        self.género= género
        self.edad= edad
        print("Se ha creado una persona nueva con", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.género, self.edad)
#Crear x persona, agregarla a una lista de un fichero externo y acceder a ese fichero con las personas
class ListaPersonas():
    def __init__(self):
        self.listaDePersonas = []
        try:
            archivo = open("listaDePersonas1", "rb")
            self.listaDePersonas = pickle.load(archivo)
            archivo.close()
        except:
            pass

    def agregarPersona(self,p):
        self.listaDePersonas.append(p)
        archivo = open("listaDePersonas1", "wb")
        pickle.dump(self.listaDePersonas, archivo)
        archivo.close()




p1 = Persona("Ángel José", "Hombre", 14)
Lista = ListaPersonas()
Lista.agregarPersona(p1)
print(Lista)

for i in Lista.listaDePersonas:
    print(i)

