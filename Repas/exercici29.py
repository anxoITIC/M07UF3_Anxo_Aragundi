def valors():
    valor1 = int(input("Introdueix un valor qualsevol: "))
    valor2 = int(input("Introdueix un altre valor: "))

    digit = 0
    if valor1 < valor2:
        digit = valor1
        while digit <= valor2:
            print(digit)
            digit = digit + 1
    else:
        digit = valor2
        while digit <= valor1:
            print(digit)
            digit = digit + 1

    print(f"{valor1} + {valor2} = {valor1 + valor2}")




valors()