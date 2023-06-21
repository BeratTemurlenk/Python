


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




#stap 2
def get_hoorntje_bakje(aantal_bolletjes):
    if aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
        print(f'Hier is uw bakje met {aantal_bolletjes} bolletje(s).')
        return 'bakje'
    while True:
        vraag_hoorntje_bakje = input(f'Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
        if vraag_hoorntje_bakje == 'hoorntje' or vraag_hoorntje_bakje == 'bakje':
            print(f'Hier is uw {vraag_hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            break
        else:
            print('Sorry, dat snap ik niet..')
    return vraag_hoorntje_bakje
    

#stap 3
def Meer_bestellen_ofniet():
    vraag_meer_bestellen = input('Wilt u nog meer bestellen?')
    while True:
        if vraag_meer_bestellen == 'ja':
            break
        elif vraag_meer_bestellen == 'nee':
            print('Bedankt en tot ziens!')
            break
        else:
            print('Sorry, dat snap ik niet..')
    return vraag_meer_bestellen
