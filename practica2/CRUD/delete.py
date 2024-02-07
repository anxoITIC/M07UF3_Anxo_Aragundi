import psycopg2

def deletePelicula(conn, connection):
    print("delete executat")
    
    #Funció que elimina la pelicula amb id=1

    #variable amb l'instrucció en sql d'esborrar la peli amb id=1
    delete = '''DELETE FROM Pelicules
            WHERE id = 1;'''

    #executem la variable delete
    #enviar la query
    connection.execute(delete)
    #commit
    conn.commit()

    print("Pelicula esborrada correctament")

