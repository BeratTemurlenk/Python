import time
from termcolor import colored
from data import *
import math



##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    copper = copper2gold(personCash['copper'])
    silver = silver2gold(personCash['silver'])
    gold = personCash['gold']   
    platinum = platinum2gold(personCash['platinum'])
    totaal = copper + silver + gold + platinum
    print(copper)
    print(silver)
    print(gold)
    print(platinum)
    
    
    return totaal

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    totaal = ((COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS * horses) + (COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS * people)) / 50
    return totaal


##################### M04.D02.O5 #####################



def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    
    nieuwe_lijst = []

    for x in list:             
        if x[key] == value:
            nieuwe_lijst.append(x)
    
    return nieuwe_lijst





def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, "shareWith", True)

def getAdventuringFriends(friends:list) -> list:
    new_friends = []
    for x in friends:             
        if x['shareWith'] and x['adventuring'] == True:
            new_friends.append(x)
    return new_friends


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2) 

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    silverprijs_paard = (horses * COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS 
    totaal_kosten_paard = silver2gold(silverprijs_paard)
    kosten_tent = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS/7) 
    totaal = totaal_kosten_paard + kosten_tent
    return totaal


##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    antwoord = ''
    for x in items:
        if antwoord != '':
            antwoord += ', '
        antwoord +=  (str(x["amount"]) + x["unit"] +' '+ x["name"])
    return antwoord

def getItemsValueInGold(items:list) -> float:
    new_prijs = 0
    for x in items:
        prijs = x['amount'] * x['price']['amount']
        if x['price']['type'] == 'copper':
            new_prijs += copper2gold(prijs)
        if x['price']['type'] == 'silver':
            new_prijs += silver2gold(prijs)
        if x['price']['type'] == 'platinum':
            new_prijs += platinum2gold(prijs)
        if x['price']['type'] == 'gold':
            new_prijs += prijs
    return new_prijs
##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    prijs = 0
    for x in people:
        prijs += platinum2gold(x['cash']['platinum'])
        prijs += x['cash']['gold']
        prijs += silver2gold(x['cash']['silver'])
        prijs += copper2gold(x['cash']['copper'])
    return prijs

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    investors1 = []
    
    for x in investors:
        if x['profitReturn'] <= 10:
            investors1.append(x)
    return investors1


def getAdventuringInvestors(investors:list) -> list:
    real_investors = getInterestingInvestors(investors)
    real_investors1 = getAdventuringPeople(real_investors)
    return real_investors1


def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    resultaat = getAdventuringInvestors(investors)
    kosten_pi = (JOURNEY_IN_DAYS * copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY)) + (JOURNEY_IN_DAYS * copper2gold        (COST_FOOD_HORSE_COPPER_PER_DAY)) + (JOURNEY_IN_DAYS * silver2gold(COST_HORSE_SILVER_PER_DAY)) + (2 * COST_TENT_GOLD_PER_WEEK )   
    kosten_alle_i = kosten_pi * len(resultaat)
    kosten_gear = 0

    for y in resultaat:
        for x in gear:
            som = x['amount'] * x['price']['amount']
            if x['price']['type'] == 'gold':
                kosten_gear += som
            if x['price']['type'] == 'copper':
                kosten_gear += copper2gold(som)
            if x['price']['type'] == 'silver':
                kosten_gear += silver2gold(som)
            if x['price']['type'] == 'platinum':
                kosten_gear += platinum2gold(som)


    kosten_alle_i += kosten_gear
    
                

    

    
    return kosten_alle_i

    


##################### M04.D02.O10 #####################



def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    
    kostmensGoud = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    kostpaardgoud = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    totaal = (kostpaardgoud * horses) + (kostmensGoud * people)
    prijs = leftoverGold // totaal
    return prijs


def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    kostmensGoud = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    kostpaardgoud = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    totaal = (nightsInInn * (kostmensGoud * people)) + (nightsInInn * (kostpaardgoud * horses))
    return round(totaal,2)



##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    bedrag = 0
    lijst = getInterestingInvestors(investors)
    uitslag = []
    for x in lijst:
        bedrag = (profitGold / 100) * x['profitReturn']
        new_bedrag = round(bedrag,2)
        uitslag.append(new_bedrag)
    return uitslag

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    totaal = (profitGold - sum(investorsCuts)) / fellowship
    new_totaal = round(totaal,2)
    return new_totaal

##################### M04.D02.O13 #####################


def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold, interestingInvestors)
    goldCut = getAdventurerCut(profitGold,investorsCuts,len(people))

# main character krijgt goldcut + de donatie afhankelijk van het aantal avonturieren. 
# friends krijgt het goldcut min het donatie. Als het een interesting inventor is het afhankelijk of hij meegaat. 
# Als hij meegaat krijgt hij de goldcut + het percentage van het profitgold. 
# en als het een investor is die niet meegaat krijgt hij alleen percentage van het profitgold. 




    # verdeel de uitkomsten
    for person in people:
        print(investorsCuts)
    
    #     geld = platinum2gold(person['cash']['platinum']) + person['cash']['gold'] + silver2gold(person['cash']['silver']) + copper2gold(person['cash']['copper'] )
    #     if person['name'] == mainCharacter['name']:
    #        geld += (goldCut + ((len(people) - 1) * 10))
    #     if person in adventuringInvestors:
    #         geld += goldCut + 
    #     elif person in interestingInvestors:
    #         geld += investorsCuts
        
    #     earnings.append({   
    #         'name'   : person['name'],
    #         'start'  : geld,
    #         'end'    : geld + profitGold
    #     })

    return earnings

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()


















