myDict = {}

while True:
    nom = input("Nom? (Per acabar respón en blanc).")  
    if nom: 
        edat = int(input("Edat?")) 
        myDict[nom] = edat 
    else: 
        break   

print(myDict)   
