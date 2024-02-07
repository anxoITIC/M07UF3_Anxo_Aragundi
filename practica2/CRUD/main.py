import psycopg2

from conn import connexio
from createTable import creaTaula
from create import createElements
from update import updatePelicula
from delete import deletePelicula
from read import readPeliculas


try:

    print("Connexió i taula creades")
    conn, connection = connexio() #crear la connexió amb la base de dades
    creaTaula(conn, connection) #crear la taula amb els elements

    #creació d'elements
    createElements(conn, connection) #insertar elements a la taula

    readPeliculas(conn, connection) #lectura pre-update

    updatePelicula(conn, connection) #editar les dades d'una peli concreta

    readPeliculas(conn, connection) #lectura post-update

    deletePelicula(conn, connection) #esborrar una peli en concret

#excepció per si el procés falla
except (Exception, psycopg2.Error) as error:
    print("Error", error)

#al acabar tancar la connexió
finally:
    print("Procés acabat per complet.")
    conn.close()