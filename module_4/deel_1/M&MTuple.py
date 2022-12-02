import random


kleuren = ("oranje", "blauw", "groen", "bruin")
vraag = int(input('hoeveel M&Ms moeten erin '))
zakje = []

for x in range(vraag):
    randomGetal =  random.randint(0,3)
    zakje.append(kleuren[randomGetal])


print(zakje)
