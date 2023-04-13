from fruitmand import fruitmand

fruitmand.append({'name': 'watermeloen', 'weight': 900, 'color': 'green', 'round': True})


totaal = 0

for x in fruitmand:
   totaal = totaal + x['weight'] 

print(totaal)
    



     