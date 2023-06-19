JOURNEY_IN_DAYS = 11
COST_FOOD_HUMAN_COPPER_PER_DAY = 4
COST_FOOD_HORSE_COPPER_PER_DAY = 3
COST_TENT_GOLD_PER_WEEK = 3
COST_HORSE_SILVER_PER_DAY = 5




def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return amount / 50

def platinum2gold(amount:int) -> float:
    return amount * 25

# def getPersonCashInGold(personCash:dict) -> float:
#     copper = copper2gold(personCash['copper'])
#     silver = silver2gold(personCash['silver'])
#     gold = personCash['gold']   
#     platinum = platinum2gold(personCash['platinum'])
#     totaal = copper + silver + gold + platinum
    
#     return totaal

# print(2 * COST_TENT_GOLD_PER_WEEK )



# print(0.88 + 0.6599999999999999 + 11.0 + 6)




leftoverGold = 10
kostmensGoud = 3

print(leftoverGold // kostmensGoud)