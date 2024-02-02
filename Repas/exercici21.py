numeros = input("Introdueix 10 dígits separats per espais:")

#dividir la string de números en un array i passar-los a int
numeros = numeros.split()
numeros = [eval(i) for i in numeros]
sumaTotal = 0

 #recòrrer l'array i calcular la suma total
for digit in numeros:
    sumaTotal = sumaTotal + digit

#calcular la mitjana
mitjana = sumaTotal/10

#afegir els dos càlculs a l'array
numeros2 = numeros
numeros2.append(sumaTotal)
numeros2.append(mitjana)

#mostrar els resultats
print(f"Números de l'usuari: {numeros}")
print(f"Suma total: {sumaTotal}")
print(f"Mitjana: {mitjana}")
print(f"Llista actualitzada: {numeros2}")

