import psycopg2

def deletePelicula(conn, connection):
    id_borrar = int(input("ID de la pelicula a esborrar:"))
    
    #Funció que elimina la pelicula amb id=1

    #variable amb l'instrucció en sql d'esborrar la peli amb id=1
    delete = f'''
                DELETE FROM Pelicules
                WHERE id = {id_borrar};
        '''

    #executem la variable delete
    #enviar la query
    connection.execute(delete)
    #commit
    conn.commit()


    print("")
    print("Pelicula esborrada correctament")


