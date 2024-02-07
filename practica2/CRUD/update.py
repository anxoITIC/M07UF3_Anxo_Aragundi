import psycopg2

def updatePelicula(conn, connection):
    print("updatePelicula executat")

    update = '''
        UPDATE Pelicules
        SET
            titol = 'Shutter Island',
            director = 'Martin Scorsese',
            genere = 'Misteri',
            sortida = 2010,
            opinio = 'Molt bona i amb bon gir de guió'
        WHERE titol = 'The Dark Knight';
    '''

    
    #executem la variable update
    #enviar la query
    connection.execute(update)
    #commit
    conn.commit()

    print("Update fet correctament")