from collections import Counter

paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

tupla_paraules = (paraula1, paraula2)

comptador_lletres = Counter("".join(tupla_paraules))

print("Resultats:")
for lletra, comptador in comptador_lletres.items():
    print(f"{lletra}: {comptador}")
