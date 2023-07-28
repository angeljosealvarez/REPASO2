import pickle
class Coche():
    def __init__(self, marca, coche):
        self.marca= marca
        self.coche= coche
        print("Nada")
    def estado(self):
        print(self.marca, self.coche)
ficheroApertura = open("losCoches", "rb")
misCoches = pickle.load(ficheroApertura)
for c in misCoches:
    print(c.estado())
