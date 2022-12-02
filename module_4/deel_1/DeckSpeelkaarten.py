import random

types_kaarten = ["schoppen", "klaverën", "ruiten", "harten"]
speciale_kaarten = ["boer", "vrouw", "heer", "aas"]
kaarten = ["joker", "joker 2"]

for x in types_kaarten:
    for y in speciale_kaarten:
        kaarten.append(f'{x} {y}')
    for z in range(2, 11, 1):
        kaarten.append(f' {x} {z}')



random.shuffle(kaarten)



for k in range(1,8):
    kaart = random.choice(kaarten)
    print(f'kaart {k}: {kaart}')
    kaarten.remove(kaart)


print(f'de rest van de kaarten is (47):{kaarten}')