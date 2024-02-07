import psycopg2

def createElements(conn, connection):
    
    while True:   #bucle per introduïr totes les pelis que vulguis
        titol = input("Titol:")
        if not titol:   #si el títol es deixa en blanc es para
            break
        director = input("Director:")
        genere = input("Gènere:")
        sortida = input("Any de sortida:")
        opinio = input("Opinió:")

        inserts = f'''
            INSERT INTO Pelicules (titol, director, genere, sortida, opinio)
            VALUES 
            ('{titol}', '{director}', '{genere}', {sortida}, '{opinio}');
        '''

        #executem la variable inserts
        #enviar la query
        connection.execute(inserts)
        #commit
        conn.commit()

        print("")
        print("Película registrada correctament.")
        print("")
    

    print("")
    print("Procés d'inserció de dades tancat correctament")
    print("")
