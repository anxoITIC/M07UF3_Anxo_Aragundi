import random

numeroFinal = random.randint(1, 100)

trobat = False

numeroIntents = 0

while trobat == False:
    numeroIntents = numeroIntents + 1
    numero = input("Digues un número entre el 1 i el 100:")
    if numero == numeroFinal:
        trobat == True
        print("Correcte! Has necessitat {numeroIntents} intents")
    else:
        print("Incorrecte.")
    