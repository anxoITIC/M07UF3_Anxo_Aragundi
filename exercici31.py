preu = int(input("Introdueix el preu: "))
iva = int(input("Introdueix el IVA: "))

def calculaIVA(preu, iva):
    if iva not in [21, 4, 10]:
        iva = 21

    preuFinal = preu + ((preu/100) * iva)
    preuFinal = round(preuFinal, 2)

    print(f"Valor sense IVA aplicat: {preu}€")
    print(f"IVA: {iva}% ({(preu/100) * iva}€)")
    print(f"Valor amb IVA aplicat: {preuFinal}€")


calculaIVA(preu, iva)
