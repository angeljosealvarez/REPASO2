#def devuelve_generadores(*ciudades): #Va a devolver un número indeterminado de argumentos y esos argumentos van a ser en forma de tupla
    #for elemento in ciudades:
     #   yield from elemento  #Es como decirle: Hazme un yield DESDE el primer elemento 
        

#print(next(devuelve_generadores("Madrid", "Vilbao", "Barcelona")))

def devuelve_generadores(*ciudades):
    for elemento in ciudades:        
        yield elemento
generador_ciudades = devuelve_generadores("Madrid", "Lisbao")
print(next(generador_ciudades))
print(next(generador_ciudades))

