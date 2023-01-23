def naam_leeftijd () -> str:
    dictionary_naam_leeftijd = {}
    antwoord_naam = input('wat is je naam? *typ stop als je wilt stoppen*')
    if antwoord_naam == 'stop':
        antwoord_leeftijd = 10
    else:
        antwoord_leeftijd = int(input('hoe oud ben je? '))
    dictionary_naam_leeftijd['naam'] = antwoord_naam
    dictionary_naam_leeftijd['leeftijd'] = antwoord_leeftijd
    return dictionary_naam_leeftijd




lijstje = []

while True:
    mijn_dict = naam_leeftijd()
    if mijn_dict['naam'] != 'stop':
        lijstje.append(mijn_dict)
    else:
        break


for x in lijstje:
    naam = x['naam']
    leeftijd = x['leeftijd']
    print(f'{naam} is {leeftijd} jaar')
