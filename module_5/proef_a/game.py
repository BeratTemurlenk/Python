import random
from data import *

# functies

def winnaar_gevecht_character(vijand) -> bool:
    
    if vijand['hp'] <= 0:
        gevecht = False
    else:
        gevecht = True
    return gevecht       
print(winnaar_gevecht_character(lijstje_vijanden[0]))




def winnaar_gevecht_vijand(character) -> bool:     
    if character['hp'] <= 0:
        gevecht1 = False
    else:
        gevecht1 = True
    return gevecht1
print(winnaar_gevecht_vijand(lijstje_characters[0]))






# # variables/constantes


# # programmacode

# while True:
#     naam_character = input(f'''{TEKST[0]} 
#                             naam = {lijstje_characters[0]['naam']}, hp = {lijstje_characters[0]['hp']}, Attack 1 = {lijstje_characters[0]['attack_1']}
#                             Attack 2 = {lijstje_characters[0]['attack_2']}''')
    
    
    
    
    
    
    
#     if naam_character == 'robert' or naam_character == 'chyntiqa' or naam_character == 'billy':
#         print(f'goedzo, je hebt {naam_character} gekozen, succes met vechten!')
#         break
#     else:
#         try:
#             print('voer een geldige naam in!')
#         except NameError:
#             break


# print(f'{naam_character} VS {lijstje_vijanden[0]}')

# while naam_character == 'robert':
#     gevecht = True
 
        


        
        
        
        
    

# ik maak 3 characters aan. ze hebben allemaal verschillende aanvallen en hp en een ultimate.
# ik maak ook 3 vijanden aan die ook verschillend zijn met verschillende aanvallen en hp. wanneer je een karakter
# hebt gekozen vecht je tegen vijand tot en met 3. na elke gevecht krijgt de character 75 hp erbij.
# ik maak een functie aan om te bepalen of de character levend of dood uit het gevecht komt. 
# bij de 3de gevecht is het mogelijk om de character zijn ultimate te laten doen.
# als je alle 3 de vijanden verslaat heb je de game verslagen!

    
    
    
    
