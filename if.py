CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15
vraag = "ben je pc of console?"

antwoord = input(vraag)

if antwoord == 'console':
    prijs = CONSOLE_PRIJS
    if input("ben je een member") == 'ja':
        prijs -=MEMBER_KORTING

else: 
    prijs = PC_PRIJS

print(f'u bent een {antwoord} dus is het voor jou {prijs} euro')
