import psycopg2

#creació de la taula i els elements
def creaTaula(conn, connection):
        
        print("Trucada 2 feta")
    #creació de la taula
        #he decidit fer la meva base de dades sobre pelicules
        sql = '''   DROP TABLE IF EXISTS Pelicules;
                    CREATE TABLE Pelicules(    
                    id SERIAL PRIMARY KEY NOT NULL,
                    titol VARCHAR(30) NOT NULL,
                    director VARCHAR(30) NOT NULL,
                    genere VARCHAR(30) NOT NULL,
                    sortida int NOT NULL,
                    opinio VARCHAR(40) NOT NULL
        )'''


        #enviar la query
        connection.execute(sql)
        #commit
        conn.commit()

        print("Procés completat! Taula creada.")
        print("")

