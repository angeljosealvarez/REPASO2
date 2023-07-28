#USER DEFINED FUNCTIONS
import sqlite3
import pandas as pd

#AL USAR PYTHON SE ESTA HACIENDO UNA TRANSACCIÓN EN LA BASE DE DATOS





square = lambda n : n*n
print(square(10))



with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square", 1, square)
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT *, square(Price) as precio_al_cuadrado FROM Products WHERE Price > 0
        '''
    )
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

    conn.commit
    print(results_df)


"""

conn = sqlite3.connect("Northwind.db")
conn.create_function("square", 1, square) #nombre de la función que queramos poner, parámetros y la función de python

cursor = conn.cursor()
cursor.execute(
    '''
    SELECT * FROM Products
    '''
)



results = cursor.fetchall() #fetchall ejecuta la consulta y la almacena en el cursor
results_df = pd.DataFrame(results)
conn.commit()

cursor.close()
conn.close()

print(results_df)

"""