import psycopg2

try:

    #connexió amb la base de dades
    conn = psycopg2.connect(
        database="practica_crud",
        user='anxo',
        password='21022004',
        host='localhost',
        port='5432'
    )

    connection = conn.cursor()

    #creació de la taula
    #he decidit fer la meva base de dades sobre pelicules
    sql = '''CREATE TABLE Pelicules(    
                id SERIAL PRIMARY KEY NOT NULL,
                titol VARCHAR(30) NOT NULL,
                director VARCHAR(30) NOT NULL,
                genere VARCHAR(30) NOT NULL,
                any int(4) NOT NULL,
                opinio VARCHAR(40) NOT NULL
    )'''


    #enviar la query
    connection.execute(sql)
    #commit
    conn.commit()

    print("Procés completat")

#excepció per si el procés falla
except (Exception, psycopg2.Error) as error:
    print("Error", error)

#al acabar tancar la connexió
finally:
    conn.close()
