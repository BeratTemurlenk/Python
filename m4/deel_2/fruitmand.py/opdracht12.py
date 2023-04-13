from fruitmand import fruitmand

aantal = 0


namen1 = ''
fruit_lijst = []


for x in fruitmand:
    namen = x['name']
    kleur = x['color']
    
    
    if len(namen) > len(namen1):
        namen1 = namen
        kleur1 = x['color']
        gewicht = x['weight'] / 1000


lengte = len(namen1)
print(f'{namen1} heeft {lengte} letters en heeft {kleur1} als kleur en een gewicht van {gewicht}kg ')




    

