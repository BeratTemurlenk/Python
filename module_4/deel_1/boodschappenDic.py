import random


dic_boodschappen = {}

teller = 1

while True:
    vraag = input('voeg item toe!')
    if vraag in dic_boodschappen:
        dic_boodschappen[vraag] += 1 
    else:
        dic_boodschappen.update({vraag : teller})
    vraag_doorgaan = input('wil je nog meer items?')
    if vraag_doorgaan != 'ja':
        break

        


print("-[BOODSCHAPPEN}-")

for teller, vraag in dic_boodschappen.items():
    print(f"{teller} x {vraag}")


print("-----------------")



