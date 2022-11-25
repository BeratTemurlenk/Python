small_prijs = 6
medium_prijs = 9
large_prijs = 11


vraag_hoeveel_small =  'hoeveel small pizza wil je?'
vraag_hoeveel_medium = 'hoeveel medium pizza wil je?'
vraag_hoeveel_large = 'hoeveel large pizza wil je?'
while True: 
    try:
        antwoord_hoeveel_pizza1 = int(input(vraag_hoeveel_small))
        break
    except ValueError:
        print('Geen geldig antwoord, probeer opnieuw!')
        break
while True:
    try:
        antwoord_hoeveel_pizza2 = int(input(vraag_hoeveel_medium))
        break
    except ValueError:
        print('Geen geldig antwoord, probeer opnieuw!')

while True: 
    try:
        antwoord_hoeveel_pizza3 = int(input(vraag_hoeveel_large))
        break
    except ValueError:
        print('Geen geldig antwoord, probeer opnieuw!')


prijs_small_pizza = antwoord_hoeveel_pizza1 * small_prijs
prijs_medium_pizza = antwoord_hoeveel_pizza2 * medium_prijs
prijs_large_pizza = antwoord_hoeveel_pizza3 * large_prijs
totaal_prijs = (f'{prijs_small_pizza + prijs_medium_pizza + prijs_large_pizza}')


print("-------------------------------------------Berat pizza huis--------------------------------------------------------------")
print(f'{antwoord_hoeveel_pizza1} small pizza:  {prijs_small_pizza} euro')
print(f'{antwoord_hoeveel_pizza2} medium pizza: {prijs_medium_pizza} euro')
print(f'{antwoord_hoeveel_pizza3} large pizza: {prijs_large_pizza} euro') 
print(f'Dit is je totale prijs: {totaal_prijs} euro')
print("--------------------------------------------Berat pizza huis-------------------------------------------------------------")





 




