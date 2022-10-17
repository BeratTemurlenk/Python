naam = input('Wat is jouw naam?')
verhaal = print(f'Hallo {naam}. Je bent zojuist gedropt in een verlaten griezelige bos. Jou missie is om er levend uit te komen. Veel succes.')
print("""------------------------------------------------------------------start----------------------------------------------------------------------""")

    
vraag_rugtas1 = input('Je loopt door het bos en na 10 minuten vind je een rode rugtas. Pak je het op ja of nee? ')
if vraag_rugtas1 == 'ja':
    print('je hebt een vergiftigd mesje gevonden. Wie weet heb je het later nodig.')
else:
    print('je laat het liggen.')

vraag_boomhut = input('je loopt door en vind een boomhut.je hoort geluid er van komen. Ga je de boomhut in of loop je door. 1 = boomhut in, 2 = doorlopen')
if vraag_boomhut == '1':
    vraag_vechten_vluchten = input('Holy shit, je word aangevallen door een heks en ze valt je aan. Ga je vechten of vlucht je???? 1 = vechten, 2 = vluchten ')
    if vraag_vechten_vluchten == '1' and vraag_rugtas1 == 'ja':
        print('Je verslaat de heks en steekt haar dood, je verlaat de boomhut en loopt verder.')
    if vraag_vechten_vluchten == '1' and vraag_rugtas1 == 'nee':
        print('Je had geen wapen en bent verslagen door de heks. LOSER!')
        exit()
    elif  vraag_vechten_vluchten == '2':
        print('gelukkig was je een topsporter en heb je snel de benen kunnen nemen. Je loopt verder')
elif vraag_boomhut == '2':
    print('je vermijd de boomhut en loopt verder.')

vraag_rivier = input("""Je loopt al een tijdje en vind na een 1 uur een rivier. Je kan er of door heen zwemmen of omlopen. Je bent best wel moe.
wat kies je? 1 = door heen zwemmen, 2 = omlopen""")
if vraag_rivier == '1' and vraag_rugtas1 == 'ja':
    print("""Je zwemt door de rivier heen. Jij luie flapdrol, je komt een krokodil tegen maar gelukkig heb je hem kunnen wegjagen met je vergiftigd mesje.
    je hebt het overkant gehaald en je loopt door. """)
if vraag_rivier == '1' and vraag_rugtas1 == 'nee':
     print('Je zwemt door de rivier heen. Jij luie flapdrol, je komt een krokodil tegen maar je bent onbewapend. Hij heeft je opgegeten. LOSER!')
     exit()
if vraag_rivier == '2':
    vraag_rugtas2 = input("""je loopt om. Je vind een klein zwarte tasje opgehangen aan een boom. Je twijfelt om het op te pakken.
    pak je het op? 1 = oppakken, 2 = laten liggen. """)
if vraag_rugtas2 == '1':
    print('Nice, je hebt een grapling hook gevonden, Wie weet heb je het later nodig.')
elif vraag_rugtas2 == '2':
    print('Je laat het liggen.')
if vraag_rugtas2 == '1' or vraag_rugtas2 == '2':
    print("""Je loopt verder en je vind een brug. Je loopt de brug op. Je staat in het midden van de brug en SHIT, de planken vallen naar benden en jij ook. """)
if vraag_rugtas2 == '1':
    print("""tijdens het vallen besef je je dat je een grapling hook hebt en gebruikt het om jezelf naar de overkant te krijgen.
    Je loopt door.""")
elif vraag_rugtas2 == '2':
    print('Je hebt niks om je te helpen en valt ter plekken dood. LOSER!')
    exit()
vraag_zwaard = input("""Je ziet een magisch licht. Je loopt er op af en vind een zwaard vast in een rots. Je hebt een gevoel dat je de zwaard later nog nodig hebben.
 Je wilt hem eruit trekkebn maar het lukt je niet. Je moet een vraag goed hebben. De vraag is als volgt: 'Wat was de grootste berg voordat de mount everest werd ontdekt?'""")

if vraag_zwaard == 'mount everest':
    print('goed gedaan! je hebt de vraag goed. Je pakt je zwaard op en je loopt door.')
else:
    print('helaas, je hebt de vraag niet goed. Je loopt door zonder zwaard.')

print('Je ziet het einde en loopt erop af. Ineens komt er een monster op je af!!!!')

if vraag_zwaard == 'mount everest':
    print('YES, dankzij de zwaard heb ik de monster kunnen verslaan. Je loopt het bos uit en bent klaar. Je juicht van vrede. EINDE')
else:
    print('Je probeerde het monster te verslaan maar je hebt het niet gehaald. Je bent vermoord door de monster. LOSER!')
    exit()
    