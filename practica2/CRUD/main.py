import psycopg2

from conn import connexio
from create import creaTaula

try:
    #print("1:Crear connexió i taules")
    #print("2:Esborrar taules")

    #ordre = int(input("INTRODUEIX ORDRE"))

    connexio() #crear la connexió amb la base de dades

    creaTaula() #crear la taula amb els elements




    #excepció per si el procés falla
except (Exception, psycopg2.Error) as error:
    print("Error", error)

    #al acabar tancar la connexió
finally:
    conn.close()