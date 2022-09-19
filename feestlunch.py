aantal_croissantjes = int(input('hoeveel croissantjes wil je?'))
aantal_stokbroden = int(input('hoeveel stokbroden wil je?'))
aantal_kortingbonnen = int(input('hoeveel kortingsbonnen heb je?'))

croissantjes = 0.39
stokbrood = 2.78
kortingsbon = 0.50 

prijs_croissants = aantal_croissantjes * croissantjes
prijs_stokbrood = aantal_stokbroden * stokbrood
volledig_korting = aantal_kortingbonnen * kortingsbon

totaal_prijs = prijs_croissants + prijs_stokbrood - volledig_korting

totale_prijs = round(totaal_prijs, 2)


print(f'De feestlunch kost je bij de bakker {totaal_prijs} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbroden} stokbroden als de {aantal_kortingbonnen} kortingsbonnen nog geldig zijn!')




