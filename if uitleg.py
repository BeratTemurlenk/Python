name = input('wat is je naam?')

age = int(input('wat is je leeftijd'))



if age < 18 :

    if name == 'Arnold':

        print('je krijgt een vrij kaartje')

    else:

        print(f'helaas {name} je mag nog niet naar binnen')

        print('je krijgt een sticker')

elif age >= 18 and age < 21:

    print(f'hallo {name} kom naar binnen, je mag nog geen sterke drank kopen')

else:

    (f'halo{name} je mag naar binnen en je mag ook sterke drank kopen')

   