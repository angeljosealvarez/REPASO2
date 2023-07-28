#SERIALIZACIÓN OBJETOS
import pickle
class Coche():
    def __init__(self, marca, coche):
        self.marca= marca
        self.coche= coche
        print("Nada")
    def estado(self):
        print(self.marca, self.coche)

Coche1= Coche("Marca", "Coche")
Coche2= Coche("Marca2", "Coche2")
Coche3= Coche("Marca3", "Coche3")
Coches= [Coche1, Coche2, Coche3]
fichero= open("losCoches", "wb")
pickle.dump(Coches, fichero)
fichero.close()
ficheroApertura = open("losCoches", "rb")
misCoches = pickle.load(ficheroApertura)
for c in misCoches:
    print(c.estado())


