import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor() 
"""
miCursor.execute('''CREATE TABLE PRODUCTOS ( 
ID INTEGER  PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 1º CAMBIO CLASE 41.1 UNIQUE SE UTILIZA SOLO PARA UN VALOR DE UN CAMPO NO PARA EL REGISTRO ENTERO
"""
miCursor.execute('''CREATE TABLE PRODUCTOS ( 
ID INTEGER  PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
PRECIO INTEGER,
SECCION VARCHAR(20)
)''')

productos = [ #2º CAMBIO CLASE 3.2
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?,?,?)", productos) #3º CAMBIO CLASE 3.2
miConexion.commit()
miConexion.close()