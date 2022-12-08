import random

kleuren_lijst = ["rood", "blauw", "groen", "geel", "bruin"]
vraag = int(input('hoeveel M&Ms moeten de zak in?'))
zak_dictionary = {}

teller = 1




for x in range(vraag):
    kleur = random.choice(kleuren_lijst)
    if kleur not in zak_dictionary:
        zak_dictionary.update({kleur : teller})
    else:
        zak_dictionary[kleur] += 1


print(zak_dictionary).