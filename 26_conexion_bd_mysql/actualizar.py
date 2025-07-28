import mysql.connector
from conexion_db1 import DATABASE

dtos_de_la_db = mysql.connector.connect(**DATABASE)
cursor = dtos_de_la_db.cursor()


sentencia_actualizar = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
datos_a_actualizar = ('Carlitos', 'Gardel', 40, 1)

cursor.execute(sentencia_actualizar,datos_a_actualizar)
dtos_de_la_db.commit()

cursor.close()
dtos_de_la_db.close()