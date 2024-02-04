def calculaQuadrat(lista_numeros):
    resultat = [num ** 2 for num in lista_numeros]
    return resultat


llista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultat = calculaQuadrat(llista)

print(f"Llista original: {llista}")
print(f"Llista de quadrats: {resultat}")
