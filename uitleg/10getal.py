grootste = 0
kleinste = 1000
aantal = 0

for x in range(10):
    vraag = int(input('vul een getal in boven de 0 en onder de 1000:'))
    if vraag > grootste:
        grootste = vraag
    if vraag < kleinste:
        kleinste = vraag

if vraag % 3 == 0:
    aantal += 1
        

print(grootste) 
print(kleinste)
print(aantal)
    

