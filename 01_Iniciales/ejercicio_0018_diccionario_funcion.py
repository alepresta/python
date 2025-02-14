def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'llave:{llave}, valor:{valor}')

listarTerminos(IDE='Integrated Developement Enviroment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')