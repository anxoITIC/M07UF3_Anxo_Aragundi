import psycopg2

def readPeliculas(conn, connection):
    print("Dades:")

    select = "SELECT * FROM Pelicules ORDER BY id;"

    connection.execute(select) #exectuem la query

    records = connection.fetchall() #guardem el resultat

    #mostrem els resultat recorrent la variable que els guarda
    for record in records:
        print(record)

    print("")