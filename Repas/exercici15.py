valors = []

while True:
    valor = int(input("Introdueix un valor: "))
    if valor != 0:
        valors.append(valor)
    else:
        break

valors.sort()

print(valors)