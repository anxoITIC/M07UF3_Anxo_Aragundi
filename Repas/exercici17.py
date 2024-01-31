frase = input("Escriu una frase: ")

frase = frase.split()

frase = [''.join(sorted(set(palabra), key=palabra.index)) for palabra in frase]

print(frase)