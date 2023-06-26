PRIJS_IJSBOL = 1.10
PRIJS_HORRENTJE = 1.25
PRIJS_BAKJE = 0.75





#stap 1:



def get_aantal_bolletjes():
    while True:
        try:
            aantal_bolletjes = int(input('Hoeveel bolletjes wilt u?'))    
            if aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
                break
            elif aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
                print(f'Dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes.')
                break
            elif aantal_bolletjes > 8:
                print('Sorry, zulke grote bakken hebben we niet.')
        except ValueError:
            print("Sorry dat snap ik niet...")
    return aantal_bolletjes


lijst_ijsjes = []

def totaal_aantal_bollen(aantal_bolletjes):
    lijst_ijsjes.append(aantal_bolletjes)
    totaal = sum(lijst_ijsjes)
    return totaal





dict_bak_hoorn = {'bakje': 0,
                  'hoorntje': 0}

#stap 2
def get_hoorntje_bakje(aantal_bolletjes):
    if aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f'Hier is uw bakje met {aantal_bolletjes} bolletje(s).')
        dict_bak_hoorn['bakje'] += 1
        return 'bakje'
    while True:
        vraag_hoorntje_bakje = input(f'Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
        if vraag_hoorntje_bakje == 'hoorntje':
            print(f'Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            dict_bak_hoorn['hoorntje'] += 1
            break
        elif vraag_hoorntje_bakje == 'bakje':
            print(f'Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            dict_bak_hoorn['bakje'] += 1
            break
        
        else:
            print('Sorry, dat snap ik niet..')
    return vraag_hoorntje_bakje

   




#stap 3
def Meer_bestellen_ofniet():
    while True:
        vraag_meer_bestellen = input('Wilt u nog meer bestellen?')
        if vraag_meer_bestellen == 'ja':
            break
        elif vraag_meer_bestellen == 'nee':
            print('Bedankt en tot ziens!')
            break
        else:
            print('Sorry, dat snap ik niet..')
    return vraag_meer_bestellen







    
    
    
    
