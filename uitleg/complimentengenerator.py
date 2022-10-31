from random import randint, random


aantal_complimenten = int(input("Hoeveel complimenten wil je hebben?"))
naam = input("wat is je naam?")
geweldig = 'je bent geweldig'
mooi = 'je bent mooi'
haren= 'je hebt mooie haren'
schoenen = 'je hebt mooie schoenen'

for x in range (aantal_complimenten):
    random_getal = randint(1, 4)
    if random_getal == 1:
        print(f'{geweldig}, {naam}')
    elif random_getal == 2:
            print(f'{mooi}, {naam}')
    elif random_getal == 3: 
        print(f'{haren}, {naam}')
    elif random_getal == 4:
        print(f'{schoenen}, {naam}')