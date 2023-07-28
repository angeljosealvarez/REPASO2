#BASES DE DATOS

#Conexión con bases de datos y integrar registros con bases de datos

"""

NOTACIÓN DE CHEN
ENTIDAD: REFERENCIA A UN OBJETO, REPRESENTACIÓN: CUADRADO DENTRO DE PALABRA

ATRIBUTOS SIMPLES: UN ÚNICO BALOR, REPRESENTACIÓN: CÍRCULO DENTRO DE PALABRA
ATRIBUTOS COMPUESTOS: TIENEN VARIOS VALORES DENTRO DEL PROPIO ATRIBUTO, REPRESENTACIÓN: CÍRCULO DENTRO DE PALABRA CON RAMA GENIALÓGICA
ATRIBUTO MULTIVALOR: ATRIBUTOS SIMPLES QUE TIENE VARIOS VALORES, EJEMPLO DE PUERTAS DE UNA CASA (EN UNA CASA HAY MÁS DE UNA PUERTA), REPRESENTACIÓN: 2 CÍRCULOS DENTRO DE PALABRA
ATRIBUTOS DERIVADOS: SE PUEDE OBTENER A TRAVÉS DE OTRO ATRIBUTO, REPRESENTACIÓN: BORDE PUNTEADO, (EJEMPLO, SI TE HAY UN ATRIBUTO QUE DICE QUE UNA CASA SE CONSTRUYÓ EN 2010, Y OTRO QUE DICE 
QUE ESTAMOS EN 2030, ENTONCES PASARON 20 AÑOS, ESOS 20 AÑOS ES EL ATRIBUTO DERIVADO)

KEY: SIRVE PARA IDENTIFICAR UN ATRIBUTO ESPECÍFICO (FUNCIONA COMO UN ID), REPRESENTACIÓN: CÍRCULO DENTRO DE UNA PALABRA SUBRAYADA


TABLA: ESTRUCTURAS DE DATOS ORGANIZADAS EN FILAS Y COLUMNAS (COMO LAS TABLAS DE AJEDREZ O LA TABLA PERIÓDICA)
    CAMPO: NOMBRE DE LA COLUMNA
    VALOR DEL CAMPO: CADA CELDA INDIVIDUAL
    REGISTRO: CONTIENE LA INFORMACIÓN DE TODOS LOS CAMPOS (FILAS)

INTEGER: VALOR QUE SE LE DA AL CAMPO, EXISTEN VARIOS TIPOS (BLOB, ALMACENA DATOS BINARIOS), REAL (PARA MATEMÁTICAS, ALMACENAR FLOAT), NUMERIC (NÚMEROS QUE NECESITAN PRECISIÓN MATEMÁTICA MUY ALTA, EJEMPLO PI QUE 
TIENE QUE SER CASI EXACTO)

QUERY: PREGUNTAR O PEDIR INFORMACIÓN A UNA BASE DE DATOS

FALTA DE CONGRUENCIA: DATOS EN DOS IDIOMAS DENTRO DE UNA BASE DE DATOS O UN CÓDIGO

ACCIONES BÁSICAS QUE SE CONSIDERAN CONSULTAS
LAS CONSULTAS SON ACCIONES QUE SE HACEN EN UN CÓDIGO
CREATE
READ
UPDATE
DELETE


SELECT * FROM usuarios



INSERT INTO usuarios (nombre, apellido, edad)
VALUES ("Lucas", "Dalto", "21")

"""

import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTÍCULO VARCHAR ")

miConexion.close()