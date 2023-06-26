from functions_papi import *
import math

print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')


meer_bestellen = 'ja'
while meer_bestellen == 'ja':
    aantal_bolletjes = get_aantal_bolletjes()
    totaal_bollen = totaal_aantal_bollen(aantal_bolletjes)
    hoorntje_bakje = get_hoorntje_bakje(aantal_bolletjes)
    meer_bestellen = Meer_bestellen_ofniet()




prijs_alle_bakjes = dict_bak_hoorn['bakje'] * PRIJS_BAKJE
prijs_alle_hoorntjes = dict_bak_hoorn['hoorntje'] * PRIJS_HORRENTJE
prijs_alle_bollen = totaal_bollen * PRIJS_IJSBOL



bonnetje = ''
bonnetje += (f' --------------------["Papi Gelato"]--------------------\n')
bonnetje += (   f'Bolletjes {totaal_bollen} x {PRIJS_IJSBOL} = $ {prijs_alle_bollen:.2f}\n')
if dict_bak_hoorn["hoorntje"] >= 1:      
    bonnetje += (   f'Hoorntje  {dict_bak_hoorn["hoorntje"]} x {PRIJS_HORRENTJE} = $ {prijs_alle_hoorntjes:.2f}\n')
if dict_bak_hoorn["bakje"] >= 1:      
    bonnetje += (   f'Bakjes {dict_bak_hoorn["bakje"]} x {PRIJS_BAKJE} = $ {prijs_alle_bakjes:.2f}\n')  
bonnetje += ('-------------------------------------------------------- +\n')     
Totaal = prijs_alle_bakjes + prijs_alle_bollen + prijs_alle_hoorntjes
bonnetje += (   f'Totaal                = $ {Totaal:.2f}\n')
bonnetje += ('Bedankt en tot ziens!\n')


            
print(bonnetje)
    


