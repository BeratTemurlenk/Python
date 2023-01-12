from fruitmand import fruitmand
kleur = []

for y in fruitmand:
    druif = ['druif']
    if y['name'] ==  'druif':
        fruitmand.remove(y)

for x in fruitmand:
    v = x['color']
    if v not in kleur:
        kleur.append(v)
print(kleur)


    
        
        