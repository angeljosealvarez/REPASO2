import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#COMILLA TRIPLE PARA ESCRIBIR EN VARIAS LÍNEAS Y NO SOLO EN 1
miCursor.execute('''CREATE TABLE PRODUCTOS ( 
CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
NOMBRE_ARTICULO VARCHAR(50),
PRECIO INTEGER,
SECCION VARCHAR(20)
)''')

productos = [
    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalón", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

miConexion.commit()
miConexion.close()