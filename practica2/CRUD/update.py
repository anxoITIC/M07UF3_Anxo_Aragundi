import psycopg2

def updatePelicula(conn, connection):
    
    id_canvi = int(input("ID de la pelicula a modificar:"))

    titol = input("Titol:")
    director = input("Director:")
    genere = input("Gènere:")
    sortida = int(input("Any de sortida:"))
    opinio = input("Opinió:")

    update = f'''
            UPDATE Pelicules
            SET
                titol = '{titol}',
                director = '{director}',
                genere = '{genere}',
                sortida = {sortida},
                opinio = '{opinio}'
            WHERE id = {id_canvi};
        '''

    
    #executem la variable update
    #enviar la query
    connection.execute(update)
    #commit
    conn.commit()

    print("")
    print("Update fet correctament")
    print("")