hoogte_zwembad = int(input("Hoe hoog is uw zwembad?"))
breedte_zwembad = int(input("Hoe breed is uw zwembad?"))
diepte_zwembad = int(input("Hoe diep is uw zwembad?"))
grond_totaal_zwembad = int(hoogte_zwembad * breedte_zwembad * diepte_zwembad)
uitgraven_prijs = int(grond_totaal_zwembad * 25)
afvoeren_grondprijs = int(grond_totaal_zwembad * 32.50)
totaal_prijs2 = int(uitgraven_prijs + afvoeren_grondprijs)
voorrij_kilometers = int(input('Op hoeveel kilometer woont u vandaan van ons bedrijf?'))
Voorrijkosten = voorrij_kilometers
totaal_prijs3 = uitgraven_prijs + afvoeren_grondprijs + Voorrijkosten


print('stap 1')

print(hoogte_zwembad*breedte_zwembad*diepte_zwembad)

print('stap 2')

print(f"""Offerte voor een zwembad van {hoogte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter (inhoud: xx m3)"
Uitgraven: {uitgraven_prijs} euro
Afvoeren grond:{afvoeren_grondprijs} euro
totaal: {totaal_prijs2} euro""")

print('stap 3 en 4')

if voorrij_kilometers < 50 and grond_totaal_zwembad < 20:
    Voorrijkosten = 100 + (1.25 * voorrij_kilometers)
elif voorrij_kilometers > 50 and grond_totaal_zwembad < 20:
    Voorrijkosten = 100 + (1.15 * voorrij_kilometers)
elif voorrij_kilometers < 50 and grond_totaal_zwembad > 20:
    Voorrijkosten = 250 + (2.15 * voorrij_kilometers)
elif voorrij_kilometers > 50 and grond_totaal_zwembad > 20:
    Voorrijkosten = 250 + (2.05 * voorrij_kilometers)


print(f"""Offerte voor een zwembad van {hoogte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter (inhoud: xx m3)"
Uitgraven: {uitgraven_prijs} euro
Afvoeren grond: {afvoeren_grondprijs} euro
Voorrijkosten: {Voorrijkosten} euro
totaal: {totaal_prijs3} euro""")







