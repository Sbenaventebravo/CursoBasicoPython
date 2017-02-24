#manejo de bases de datos con sqlite

import sqlite3
# se lee o crea la base de datos
conexion = sqlite3.connect("base.db")
"se crea una tabla en la base de datos"
cursor = conexion.cursor()
cursor.execute('''
               CREATE TABLE persona
               (
               id int primary key not null,
               nombre text not null,
               pais char(50)
               );
              ''')
"se aniaden registros a la base de datos"
cursor.execute("INSERT INTO persona (id, nombre, pais) values (1, 'Pedro Linares', 'Chile')")
cursor.execute("INSERT INTO persona (id, nombre, pais) values (2, 'Carlos Corcuera', 'Argentina')")
cursor.execute("INSERT INTO persona (id, nombre, pais) values (3, 'Julio Mendoza', 'Mexico')")
cursor.execute("INSERT INTO persona (id, nombre, pais) values (4, 'Rosa Loyola', 'Peru')")
cursor.execute("INSERT INTO persona (id, nombre, pais) values (5, 'Angela Paz', 'Ecuador')")


conexion.commit()
"Consultas sobre la tabla"
consulta = cursor.execute('select id,nombre from persona')
#el cursor permite ingresar lenguaje sql

for i in consulta:
    print i[0], i[1]

conexion.close()



