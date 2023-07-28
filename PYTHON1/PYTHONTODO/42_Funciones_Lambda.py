#https://www.youtube.com/watch?v=tfYLcHbjc_A&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=66
#FUNCIONES LAMBDA
#SON FUNCIONES ANÓNIMAS, SIRVEN PARA ABREVIAR, RESUMIR UNA EXPRESION NORMAL EN LAMBDA
#FUNCION SIN SIMPLIFICAR
"""def area_triangulo(b,h):
    return (b*h)/2

print(area_triangulo(5,7))"""

area_triangulo = lambda base,altura:(base*altura)/2
print(area_triangulo(5,7))

al_cubo = lambda numero:pow(3)

destacar_valor = lambda comision:"¡{}!$".format(comision)
comision_Ana = 1000050000
print(destacar_valor(comision_Ana))