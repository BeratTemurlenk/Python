import random

# # variables/constantes


attack_robert = random.randint(30,40)
attack_chyntiqa = random.randint(50,60)
attack_billy = random.randint(20,30)



lijstje_characters = [{'naam': 'robert',
                      'hp': 150,
                      'attack': attack_robert,
                      'defend': 30},
                    
                    {'naam': 'chyntiqa',
                      'hp': 100,
                      'attack': attack_chyntiqa,
                      'defend': 10},                    

                    {'naam': 'billy',
                      'hp': 200,
                      'attack': attack_billy,
                      'defen': 50}]


lijstje_vijanden = [{'naam': 'sean',
                    'hp': 100,
                    'attack_1': 20,
                    'attack_2': 35},
                    {'naam': 'tobias',
                    'hp': 150,
                    'attack_1': 30,
                    'attack_2': 45},
                    {'naam': 'marnix',
                    'hp': 200,
                    'attack_1': 40,
                    'attack_2': 55}]


# functies

def functie(vijand,naam):
    while True:
        print('het gevecht is begonnen')
        karakter_zet = input('val je aan(1) of gebruik je defence(2)')
        if karakter_zet == '1':
            for x in vijand:
                lijstje_vijanden[x]['hp'] -=  lijstje_characters[naam]['attack']
                print(x)
                print(lijstje_vijanden[x]['hp'])
                print([naam]['attack'])
        
    
            








# # programmacode


for karakter in lijstje_characters:
    naam_character = print(f'''
                            naam = {karakter['naam']}, hp = {karakter['hp']}, Attack = {karakter['attack']}
                            ''')
    
gekozen_naam = input("Welkom bij mijn nieuwe game. Kies uit een character door zijn / haar naam te typen. ")

functie(lijstje_vijanden,gekozen_naam)




    
while True:   
    if gekozen_naam == 'robert' or gekozen_naam == 'chyntiqa' or gekozen_naam == 'billy':
        print(f'goedzo, je hebt {gekozen_naam} gekozen, succes met vechten!')
        break
    else:
        try:
            print('voer een geldige naam in!')
        except NameError:
            break


        


        
        
        
        
    



    
    
    
    
