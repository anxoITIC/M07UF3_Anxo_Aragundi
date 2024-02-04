import random

def sumaValors():
    valor1 = int(input("Introdueix un valor qualsevol: "))
    valor2 = int(input("Introdueix un altre valor: "))

    print(random.randint(valor1, valor2))


sumaValors()