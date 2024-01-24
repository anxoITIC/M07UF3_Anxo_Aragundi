preuInicial = int(input("Introdueix el preu brut"))

iva = int(input("Introdueix el percentatge d'IVA"))

preuFinal = int(preuInicial + ((preuInicial / 100) * iva))

print(preuInicial)
print(iva)
print(preuFinal)