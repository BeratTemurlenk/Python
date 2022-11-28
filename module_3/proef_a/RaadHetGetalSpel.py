import random

teller = 0

begin_vraag = input('wil je het leuke raad spel spelen?')

if begin_vraag != 'nee':
    print('het spel is begonnen')

for x in range(20):
    if begin_vraag == 'nee':
        break
    nummer = random.randint(1,1000)
    print(nummer)
    for x in range(10):
        raad_vraag = int(input('raad het getal!'))
        if raad_vraag == nummer:
            print('geraden')
            teller += 1
            break
        verschil_geraden = abs(raad_vraag - nummer)
        if raad_vraag > nummer:
            print('lager')
        elif raad_vraag < nummer:
            print('hoger')
        if verschil_geraden <= 20:
            print('je bent heel warm')
        elif verschil_geraden <= 50:
            print('je bent warm')
    
    print(f' je hebt {teller} punten')
    
    ronde_vraag = input('nog een getal raden?')
    if ronde_vraag != 'ja':
        break

print(f'je hebt {teller} punten!')