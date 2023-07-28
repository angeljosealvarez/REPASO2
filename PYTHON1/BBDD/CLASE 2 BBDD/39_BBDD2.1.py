import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor = miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#miCursor.execute("INSERT INTO Productos VALUES('BALON', 15, 'DEPORTES')")
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria"),  
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miConexion.commit()
miConexion.close()