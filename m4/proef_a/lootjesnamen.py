import random

namenLijst1 = []
namenlijst2 = []





while True:
    namen_vraag = input('wat is je naam?')
    if namen_vraag not in namenLijst1:
        namenLijst1.append(namen_vraag)
        namenlijst2.append(namen_vraag)
    elif namen_vraag in namenLijst1:
        print('deze naam word al gebruikt!')
    if len(namenLijst1) >= 3:
        lootjes_vraag = input('wil je nu al beginnen met lootjes trekken?')
        if lootjes_vraag == 'ja' and len(namenLijst1) >= 3:
            break

   
    



teller2 = 0

while True:
    if namenLijst1[teller2] == namenlijst2[teller2]:
        random.shuffle(namenlijst2)
        teller2 = 0
    else:
        teller2 += 1

    if teller2 == len(namenLijst1):
        break


teller4 = 0
for x in namenLijst1:
    print(f'{namenLijst1[teller4]} heeft {namenlijst2[teller4]}')
    teller4 += 1















    





