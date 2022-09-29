vraag_man_vrouw = input('Bent u een man of een vrouw?')
if vraag_man_vrouw == 'man':
    vraag_snor = input('heeft u een snor?')
    if vraag_snor == 'ja':
        snor_breed = int(input('Hoe breed is uw snor (in centimeters)'))
if vraag_man_vrouw == 'vrouw':
    vraag_kleur = input('welk kleur haar heeft u?')
    if vraag_kleur == 'rood':
        lengte_haar = int(input('Hoe lang is uw haar (in centimeters)?'))

vraag_mbo = input('Ben jij in bezit van een Diploma MBO-4 ondernemen?')
vraag_rijbewijs_vrachtwagen = input('Ben jij in bezit van een geldig Vrachtwagen rijbewijs?')
vraag_hoed = input('Ben jij in bezit van een hoge hoed?')
vraag_gewicht = int(input('Hoeveel kilo weegt u?'))
vraag_lengte = int(input('Hoelang bent u (in centimeters)?'))
vraag_certificaat = input('Heeft u een Certificaat “Overleven met gevaarlijk personeel”?')
vraag_dieren_dressuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?'))
vraag_jongleren = int(input('Hoeveel jaar praktijkervaring heeft u met jongleren?'))
vraag_acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?'))




if (vraag_man_vrouw == 'man' and vraag_snor == 'ja' and snor_breed  >9) or (vraag_man_vrouw == 'vrouw' and vraag_kleur == 'rood' and lengte_haar >19) and vraag_mbo == 'ja' and vraag_rijbewijs_vrachtwagen == 'ja' and vraag_hoed == 'ja' and vraag_gewicht >90 and vraag_gewicht <120 and vraag_lengte >150 and vraag_lengte <220 and vraag_certificaat == 'ja' and vraag_dieren_dressuur > 3 and vraag_jongleren >4 and vraag_acrobatiek >3:
    print('Je bent geschikt!')
else:
    print('je bent niet geschikt!')

    