input = input("Introdueix 10 valors separats cadascún per un espai: ")

input = input.split()

input = [eval(i) for i in input] #convertir la llista de strings a integers

input.sort()

print(input)