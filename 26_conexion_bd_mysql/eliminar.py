import mysql.connector
from conexion_db1 import DATABASE

personas_db = mysql.connector.connect(**DATABASE)
cursor = personas_db.cursor()

sentencia_eliminar = 'DELETE FROM personas WHERE id=%s'
valor_id = (1,)

cursor.execute(sentencia_eliminar,valor_id)
personas_db.commit()

print('Objeto eliminado')
personas_db.close()
