weekdagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

for x in weekdagen:
    print(f'Alle dagen van de week zijn: {weekdagen}')
    if x == 'maandag':
        break



for x in range(5):
    print(f'De werkdagen zijn: {weekdagen[x]}')


for y in range(5, 7):
    print(f'de weekenddagen zijn: {weekdagen[y]}')

for o in range(6, -1, -1):
    print(f'Alle dagen van de week in omgekeerde volgorde zijn: {weekdagen[o]}')


for y in range(4,  -1, -1):
    print(f'De werkdagen in omgekeerde volgorde zijn: {weekdagen[y]}')

for k in range(6,  4, -1):
    print(f'De weekenddagen in omgekeerde volgorde zijn: {weekdagen[k]}')














# a = ("0", "1", "2", "3", "4", "5")

# for x in a:
#     print(x)


# if '3' in a:
#     print('banaan')
# else:
#     print('appel')
    
    