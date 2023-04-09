import random



naam = input('welkom, wat is je naam?')

print(f'hallo {naam}. Welkom bij de Enemy Slayer. Om deze game te verslaan moet je  alle enemies verslaan. SUCCES! ')

player_attack = random.randint(30,50)
player_defence = 10


print('je komt je eerste enemy tegen')

while True:
    gevecht = int(input(f' gebruik je attack(1) = {player_attack} of defence(2) = {player_defence}'))
    enemy_1_hp = 125
    if gevecht == '1':
        enemy_1_hp -= player_attack
    elif gevecht == '2':
        player_defence += 10
        print(f'enemy heeft {enemy_1_hp} over')



