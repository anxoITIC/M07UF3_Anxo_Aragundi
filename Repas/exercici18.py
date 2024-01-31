paraules = []

while len(paraules) < 2:
    paraula = input("Introdueix una paraula: ")
    paraules.append(paraula)

for paraula in paraules:
    for lletra in paraula:
        