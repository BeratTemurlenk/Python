from fruitmand import fruitmand


gewicht_lijst = []    
fruit_lijst = []

for x in fruitmand:
    gewicht = x['weight'] / 1000
    fruit_naam = x['name']
    fruit_lijst.append(fruit_naam)
    gewicht_lijst.append(gewicht)
    gewicht_lijst.sort(reverse=True)

print(gewicht_lijst)
print(fruit_lijst)


    