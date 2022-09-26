# optellen, aftrekken, volgorde: kleinste grootste
getal1 = int(input("voer getal 1 in."))
getal2 = int(input("voer getal 2 in."))
actie = input("Welke actie wenst u, kies: (o)ptellen, (a)ftrekken, (k)volgorde, (g)root, (v)ermenigvuldigen, (d)elen")



if actie == 'a':
    zin = 'aftrekken'
    antwoord = getal1 - getal2
elif actie == 'v':
    zin = 'vermenigvuldigen'
    antwoord = getal1 * getal2
elif actie == 'd':
    zin = 'delen'
    if getal2 == 0:
        zin = 'je kan niet delen door 0'
    
    else:
        antwoord = getal1 / getal2

elif actie == 'o':
    zin = 'optrekken'
    antwoord = getal1 + getal2    
elif actie == 'k':
    if getal1 > getal2:
        zin = str(getal2)+ ',  ' + str(getal1)
    else:
        zin = str(getal1)+ ',  ' + str(getal2)
elif actie == 'g':
    if getal1 > getal2:
        zin = str(getal1)+ ',  ' + str(getal2)
    else:
        zin = str(getal2)+ ',  ' + str(getal1)






print(zin)
if actie != 'k' and actie != 'g':
    print(antwoord)
