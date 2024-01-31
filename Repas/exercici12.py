tuplaMesos = ("", "Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Septembre", "Octubre", "Novembre", "Desembre")

finalitzat = True

while finalitzat == True:
    valor = int(input("Introdueix un número entre el 1 i el 12: "))
    if valor == 0:
        finalitzat = False
    else:
        print(tuplaMesos[valor])


