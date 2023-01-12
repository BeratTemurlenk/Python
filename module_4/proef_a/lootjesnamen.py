import random

namenLijst1 = []
namenlijst2 = []

teller = 0



while True:
    namen_vraag = input('wat is je naam?')
    if namen_vraag not in namenLijst1:
        namenLijst1.append(namen_vraag)
        namenlijst2.append(namen_vraag)
    teller += 1
    lootjes_vraag = input('wil je nu al beginnen met lootjes trekken?')
    if lootjes_vraag in namenLijst1:
        print('naam zit er al in')
    if teller < 3 and lootjes_vraag == 'ja':
        print('je moet minimaal 3 unieke namen invullen!')
        continue
    elif teller >= 3 and lootjes_vraag == 'ja' and len(namenLijst1) >= 3:
        break
    elif teller >= 3 and lootjes_vraag == 'ja' and len(namenLijst1) <= 3:
        print('je moet minimaal 3 unieke namen invullen!')
        continue
    elif teller < 3 or teller >= 3 and lootjes_vraag != 'nee':
        continue   
    



teller2 = 0
checker = 0
while True:
    if namenLijst1[teller2] == namenlijst2[teller2]:
        random.shuffle(namenlijst2)
        checker = 0
        teller2 = 0
    else:
        checker += 1
        teller2 += 1

    if checker == len(namenLijst1):
        break


teller4 = 0
for x in namenLijst1:
    print(f'{namenLijst1[teller4]} heeft {namenlijst2[teller4]}')
    teller4 += 1















    





