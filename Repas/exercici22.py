import xml.etree.ElementTree as ET

#primer apartat del xml
students = ET.Element('students') 

n = 1
while n <= 5:

    #segon apartat dins del primer
    student = ET.SubElement(students, 'student')

    #apartats dins del segon apartat
    name = ET.SubElement(student, 'name')
    surname = ET.SubElement(student, 'surname')
    email = ET.SubElement(student, 'email')
    dni = ET.SubElement(student, 'dni')

    #posar contingut dins del xml (fent-ho cinc vegades)

    name.text = 'Nom' + str(n)
    surname.text = 'Cognom' + str(n)
    email.text = 'Correu' + str(n)
    dni.text = 'DNI' + str(n)

    n+=1


print(ET.dump(students))


