from operator import truediv
from pickle import FALSE


gastheer = input('Wie is de gastheer')
gasten = True
drank = True
chips = False

if (gastheer == 'berat' and drank) or (gasten and drank and chips) or (gasten and drank and chips and gastheer == 'berat'):
    print('start the party')
else:
    print('No party')