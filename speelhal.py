toegangsticket = 7.45
vip_prijs_per_minuut = 0.37 / 5
aantal_personen =  int(input(" hoeveel personen ?"))


totaal_toegangsprijs = aantal_personen * toegangsticket


aantal_minuten =  int(input(" Hoeveel minuten vip wil je ?"))

totaal_vipprijs = aantal_minuten * vip_prijs_per_minuut 


print(totaal_toegangsprijs + (totaal_vipprijs * aantal_personen ))

prijs = totaal_toegangsprijs + totaal_vipprijs * aantal_personen 

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met 45 minuten VR kost je maar {prijs}')