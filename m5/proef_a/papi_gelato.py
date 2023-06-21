from functions_papi import *
  

print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.')
meer_bestellen = 'ja'
while meer_bestellen == 'ja':
    aantal_bolletjes = get_aantal_bolletjes()
    hoorntje_bakje = get_hoorntje_bakje(aantal_bolletjes)
    meer_bestellen = Meer_bestellen_ofniet()



