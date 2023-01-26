# vraagt een getal aan de gebruiker en geeft deze terug
# def vraag_een_getal(vraag: str) -> int:         #betekent definieer = maak aan

#     while True:
#         try:
#             getal = int(input('voer leeftijd in:'))
#             break
#         except ValueError:
#             print('opnieuw')
#             continue

#     return getal

# leeftijd = vraag_een_getal('voer leeftijd in:')





# def antwoord_terug(vraag: str) -> str:
    
#     vraag = input('wat is je naam:')
#     return vraag.lower()



# vraag_2 = antwoord_terug('wat is je naam:')


# def waar_of_niet_waar(antwoord: str) -> bool:

#     vraag_getal1 = int(input('voer getal 1 in:'))
#     vraag_getal2 = int(input('voer getal 2 in:'))
#     if vraag_getal1 == vraag_getal2:
#         antwoord = True
#     else:
#         antwoord = False
#     return antwoord

# vraag_getal1 = waar_of_niet_waar('voer getal 1 in:')
# vraag_getal2 = waar_of_niet_waar('voer getal 2 in:')



def bereken_btw_over_bedrag(bedrag: float, btw_percentage: int) -> float:
    bedrag_inc = (bedrag * (100 + btw_percentage)) / 100
    return round(bedrag_inc ,2)

bedrag_exclusief = 100
bedrag_exclusief = bereken_btw_over_bedrag(bedrag_exclusief, 21)

print(bedrag_exclusief)