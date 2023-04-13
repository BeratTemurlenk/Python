som = 50
telgetal = 50
zin = '50'

while som < 1000:
    telgetal += 1
    som = som + telgetal
    zin += (f' + {telgetal} ')
    print(f'{zin} = {som}')
    
