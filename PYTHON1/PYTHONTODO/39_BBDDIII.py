#CLASE 3
import sqlite3
miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute("""
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,  
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))

""")    

productos = [

    ( "pelota", 10, "Deportes"),
    ( "voley", 90, "Cerámica"),
    ( "voley2", 20, "Juguetería"),
    ( "voley3", 40, "ferretería")

]


miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos) #NO DEJA PONER AR03 YA QUE AL SER PRIMARYKEY YA EXISTE
miConexion.commit()
miConexion.close()
