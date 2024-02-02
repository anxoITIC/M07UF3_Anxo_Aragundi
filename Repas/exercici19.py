areas_pis = ['Menjador', 10.15, 'Rebedor', 9.56, 'Habitació1', 12.34, 'Terrassa', 15.55, 'Lavabo', 7.98, 'Cuina', 12, 'Habitació2', 12.23]

#Imprimir del primer element al tercer element
print(areas_pis[0], areas_pis[1], areas_pis[2])

#Imprimir del tercer element a l’últim
print(areas_pis[2:])

#Imprimir el total de l'àrea de les dues habitacions
print(areas_pis[4], areas_pis[5])
print(areas_pis[-2], areas_pis[-1])

#Modificar l’àrea del lavabo i imprimir la nova list area
areas_pis[9] = 6.53
print(areas_pis)


#Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
areas_pis.append('Pati interior')
areas_pis.append(2.78)
print(areas_pis)

#àrea total del pis
print(areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] +  areas_pis[9] + areas_pis[11] + areas_pis[13] + areas_pis[15], str('metres quadrats'))

