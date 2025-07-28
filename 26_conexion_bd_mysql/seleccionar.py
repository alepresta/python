import mysql.connector
from conexion_db1 import DATABASE

personas_db = mysql.connector.connect(**DATABASE)
mi_cursor = personas_db.cursor()
sentencia1= 'SELECT id, nombre, apellido, edad FROM personas'
sentencia0= 'SELECT * FROM personas'
mi_cursor.execute(sentencia0)

resultado = mi_cursor.fetchall()
for persona in resultado:
    print(persona)

personas_db.close()
