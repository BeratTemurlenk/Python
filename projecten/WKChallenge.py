vraag_land1 = input('voer de eerste land in voor groep A ')
vraag_land2 = input('voer de tweede land in voor groep A ')
vraag_land3 = input('voer de derde land in voor groep A ')


punten1 = 0
punten2 = 0
punten3 = 0

goal_gemaakt1 = int(input(f'hoeveel goals werden door {vraag_land1} gemaakt?'))
goal_gemaakt2 = int(input(f'hoeveel goals werden door {vraag_land2} gemaakt?'))
goal_gemaakt3 = int(input(f'hoeveel goals werden door {vraag_land3} gemaakt?'))
goal_gemaakt4 = int(input(f'hoeveel goals werden door {vraag_land1} gemaakt?'))
goal_gemaakt5 = int(input(f'hoeveel goals werden door {vraag_land2} gemaakt?'))
goal_gemaakt6 = int(input(f'hoeveel goals werden door {vraag_land3} gemaakt?'))


doelsaldo1 = 0
doelsaldo2 = 0
doelsaldo3 = 0

if goal_gemaakt1 > goal_gemaakt2:
    punten1 += 3
    doelsaldo1 += goal_gemaakt1
    doelsaldo2 += goal_gemaakt2
if goal_gemaakt1 < goal_gemaakt2:
    punten2 += 3
    doelsaldo1 += goal_gemaakt1 
    doelsaldo2 += goal_gemaakt2
if goal_gemaakt2 > goal_gemaakt3:
    punten2 += 3
    doelsaldo2 += goal_gemaakt2
    doelsaldo3 += goal_gemaakt3
if goal_gemaakt2 < goal_gemaakt3:
    punten3 += 3
    doelsaldo2 += goal_gemaakt2
    doelsaldo3 += goal_gemaakt3
if goal_gemaakt4 > goal_gemaakt3:
    punten1 += 3
    doelsaldo1 += goal_gemaakt1
    doelsaldo3 += goal_gemaakt3
if goal_gemaakt4 < goal_gemaakt3:
    punten3 += 3
    doelsaldo1 += goal_gemaakt1
    doelsaldo3 += goal_gemaakt3
if goal_gemaakt5 > goal_gemaakt4:
    punten2 += 3
    doelsaldo2 += goal_gemaakt2
    doelsaldo1 += goal_gemaakt1
if goal_gemaakt5 < goal_gemaakt4:
    punten1 += 3
    doelsaldo2 += goal_gemaakt2
    doelsaldo1 += goal_gemaakt1
if goal_gemaakt6 > goal_gemaakt5:
    punten3 += 3
    doelsaldo3 += goal_gemaakt3
    doelsaldo2 += goal_gemaakt2
if goal_gemaakt6 < goal_gemaakt5:
    punten2 += 3
    doelsaldo3 += goal_gemaakt3
    doelsaldo2 += goal_gemaakt2





















































print(f'''---------------------------------------------------------------------------------------------------------------------------
        Land:                                   Doelsaldo:                                                     Puntentotaal:
        {vraag_land1}                            {doelsaldo1}                                                              {punten1}
        {vraag_land2}                             {doelsaldo2}                                                               {punten2}
        {vraag_land3}                              {doelsaldo3}                                                              {punten3}
            
          ---------------------------------------------------------------------------------------------------------------------------
''')