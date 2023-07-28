import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor() 
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')") #1º CAMBIO DE LA CLASE 3.2
miCursor.execute('''CREATE TABLE PRODUCTOS ( 
ID INTEGER  PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50),
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