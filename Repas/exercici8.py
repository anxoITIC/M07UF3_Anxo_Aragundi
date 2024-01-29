paraules = input("Introdueix entre 1 i 3 paraules: ")

paraules_separades = paraules.split()

if 1 <= len(paraules_separades) <= 3:
    for paraula in paraules_separades:
        # Mostrar la paraula
        print(f"Paraula: {paraula}")
        
        quantitat_caracters = len(paraula)
        print(f"Quantitat de caràcters: {quantitat_caracters}")
        
        primer_caracter = paraula[0]
        print(f"Primer caràcter: {primer_caracter}")
        
        ultim_caracter = paraula[-1]
        print(f"Últim caràcter: {ultim_caracter}")
