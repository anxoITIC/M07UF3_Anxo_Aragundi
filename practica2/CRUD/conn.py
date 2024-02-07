import psycopg2

#connexió del codi amb la base de dades
def connexio():

    #connexió amb la base de dades
    conn = psycopg2.connect(
        database="practica_crud",
        user='anxo',
        password='21022004',
        host='localhost',
        port='5432'
    )

    connection = conn.cursor()

    return conn, connection


