from fruitmand import fruitmand
import random



vraag = int(input('aantal?'))




for x in range(vraag):
    random1 = random.randint(0,(len(fruitmand)-1))
    print(fruitmand[random1]['name'])