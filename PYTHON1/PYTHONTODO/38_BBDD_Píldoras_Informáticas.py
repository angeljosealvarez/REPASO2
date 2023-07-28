"""
import sqlite3

miConexion = sqlite3.connect("BBDDPildoras")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #VARCHAR ES STR Y EL PARÁMETRO ES EL NÚMERO DE CARÁCTERES QUE VA A ALMACENAR

miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
miConexion.commit()
"""

#---------------------------------------------------------------------------

#CLASE 2

import sqlite3
miConexion = sqlite3.connect("BBDDPildoras")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))") #VARCHAR ES STR Y EL PARÁMETRO ES EL NÚMERO DE CARÁCTERES QUE VA A ALMACENAR
"""
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
miConexion.commit()

variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miConexion.commit()
"""
#EJECUTAR EL CÓDIGO







miCursor.execute("SELECT * FROM PRODUCTOS")
resultado = miCursor.fetchall()
for i in resultado:
    print("Nombre artículo:  ", i[0], "Sección: ", i[2])

