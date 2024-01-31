import random

numeroFinal = random.randint(1, 100)

intents = 1

valor = int(input("Digues un número: "))

while valor != numeroFinal:
    if valor > numeroFinal:
        valor = int(input("Incorrecte. El número a endevinar és més petit:"))
    else:
        valor = int(input("Incorrecte. El número a endevinar és més gran: "))
    intents = intents + 1

print("Correcte!")
print("Has necessitat " + str(intents) + " intents.")