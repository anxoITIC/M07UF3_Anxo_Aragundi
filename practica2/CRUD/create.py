import psycopg2

def createElements(conn, connection):
    print("createElements executat")

    inserts = '''
        INSERT INTO Pelicules (titol, director, genere, sortida, opinio)
        VALUES 
        ('Inception', 'Christopher Nolan', 'Ciència Ficció', 2010, 'MOLT bona'),
        ('Django Unchained', 'Quentin Tarantino', 'Western', 2012, 'De les meves preferides'),
        ('The Dark Knight', 'Christopher Nolan', 'Acció', 2008, 'No sé perquè em vaig avorrir una mica'),
        ('Catch Me If You Can', 'Steven Spielberg', 'Basada en fets reals', 2003, 'Molt bona i divertida');
    '''
    
    #executem la variable inserts
    #enviar la query
    connection.execute(inserts)
    #commit
    conn.commit()

    print("Inserts fets correctament")