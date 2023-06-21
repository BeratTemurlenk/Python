
print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')


#stap 1:
while True:
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
    


    aantal_bolletjes = get_aantal_bolletjes()

#stap 2
    def get_hoorntje_bakje():
        while aantal_bolletjes >= 1 and aantal_bolletjes <= 3:
            vraag_hoorntje_bakje = input(f'Wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
            if vraag_hoorntje_bakje == 'hoorntje' or vraag_hoorntje_bakje == 'bakje':
                pass
            else:
                print('Sorry, dat snap ik niet..')
            return vraag_hoorntje_bakje
        if aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
            pass
            


    hoorntje_bakje = get_hoorntje_bakje()

#stap 3
    def Meer_bestellen_ofniet():
        while hoorntje_bakje == 'hoorntje' or hoorntje_bakje == 'bakje':
            print(f'Hier is uw {hoorntje_bakje} met {aantal_bolletjes} bolletje(s).')
            break
        while aantal_bolletjes >= 4 and aantal_bolletjes <= 8:
            print(f'Hier is uw bakje met {aantal_bolletjes} bolletje(s).')
            break
        vraag_meer_bestellen = input('Wilt u nog meer bestellen?')
            
        if vraag_meer_bestellen == 'ja':
            pass
        elif vraag_meer_bestellen == 'nee':
            print('Bedankt en tot ziens!')
            return vraag_meer_bestellen
        else:
            print('Sorry, dat snap ik niet..')


        
        


    meer_bestellen = Meer_bestellen_ofniet()
    break
    

