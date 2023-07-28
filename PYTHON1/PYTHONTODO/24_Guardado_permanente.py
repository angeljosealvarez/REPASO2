import pickle
class Persona():
    def __init__(self, nombre, género, edad):
        self.nombre= nombre
        self.género= género
        self.edad= edad
        print("Se ha creado una persona nueva con", self.nombre)
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.género, self.edad)
class ListaPersonas():
    personas = []
    def __init__(self):
        listaDePersonas= open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            listaDePersonas.close()
    def agregarPersonas(self, p):
        self.personas.append(p)
        listaDePersonas= open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
    def mostrarPersonas(self, p):
        for p in self.personas:
            print(p)
    def mostarInfo(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

        
        
miLista = ListaPersonas()
p1= Persona("Sandra", "Femenino", "29")
miLista.agregarPersonas(p1)
p2= Persona("Manolo", "Femenino", "29")
miLista.agregarPersonas(p2)
p3= Persona("Lucas", "Femenino", "29")
miLista.agregarPersonas(p3)
p4= Persona("Lucas", "Femenino", "29")
miLista.agregarPersonas(p4)
miLista.mostarInfo()