
def tafel_getal (aantal):
    antwoord = ''
    for x in range(1,11):
        antwoord += (f'{x} x {aantal} = {x * aantal} \n')
    return antwoord

tafel = int(input('Van welk getal wilt u de tafel zien? '))
print(tafel_getal(tafel))








