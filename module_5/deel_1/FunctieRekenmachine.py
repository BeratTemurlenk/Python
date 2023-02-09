from functieHelp import *



def addition(number1, number2):
    antwoord_plus = number1 + number2
    return antwoord_plus


def subtraction(number1, number2):
    antwoord_min = number1 - number2
    return antwoord_min

def multiplication(number1, number2):	
    antwoord_keer = number1 * number2
    return antwoord_keer

def division(number1, number2):
    antwoord_delen = number1 / number2
    
    return antwoord_delen




choice = input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?')


if choice == 'E' or choice == 'F':
    nummer2 = 1
    nummer1 = get_float_int('voer getal 1 in')
elif choice == 'G' or choice == 'H':
    nummer2 = 2
    nummer1 = get_float_int('voer getal 1 in')
else:
    nummer1 = get_float_int('voer getal 1 in')
    nummer2 = int(input('vul getal 2 in!'))
   

if choice == 'A':
    plus = print(addition(nummer1, nummer2))
elif choice == 'B':
    min = print(subtraction(nummer1, nummer2))
elif choice == 'C':
    keer = print(multiplication(nummer1, nummer2))
elif choice == 'D':
    delen = print(division(nummer1, nummer2))
elif choice == 'E':
    print(nummer1 + nummer2)
elif choice == 'F':
    print(nummer1 - nummer2)
elif choice == 'G':
    print(nummer1 * nummer2)
elif choice == 'H':
    print(nummer1 / nummer2)
    


