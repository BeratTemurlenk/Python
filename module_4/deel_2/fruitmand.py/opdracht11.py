from fruitmand import fruitmand

ronde_fruit = 0
niet_ronde_fruit = 0
vraag_kleur = ''
kleuren = []

for fruit in fruitmand:
    y = fruit['color']
    kleuren.append(y)

while True:
    vraag_kleur = input('voer een kleur in!')
    if vraag_kleur in kleuren:
        break
    else:
        print(f'De kleur {vraag_kleur} zit niet in de fruitmand')
for fruit2 in fruitmand:
    if fruit2['color'] == vraag_kleur:
        if fruit2['round'] == True:
            ronde_fruit +=1
        else: 
            niet_ronde_fruit += 1


if ronde_fruit > niet_ronde_fruit:
    totaal_ronde = ronde_fruit - niet_ronde_fruit 
    print(f'Er zijn {totaal_ronde} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}')
elif niet_ronde_fruit > ronde_fruit:
    totaal_niet_ronde = niet_ronde_fruit - ronde_fruit
    print(f'Er zijn {totaal_niet_ronde} meer ronde vruchten dan niet ronde vruchten in de kleur {vraag_kleur}')
else:
    print(f'Er zijn {ronde_fruit} ronde vruchten en {niet_ronde_fruit} niet ronde vruchten in de kleur {vraag_kleur}')