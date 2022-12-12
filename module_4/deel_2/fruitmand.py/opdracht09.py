from fruitmand import fruitmand
kleur = []

fruitmand.pop(4)

for x in fruitmand:
    v = x['color']
    if v not in kleur:
        kleur.append(v)
print(kleur)


    
        
        