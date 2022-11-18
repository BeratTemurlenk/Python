# name of student: Berat Temurlenk
# number of student: 99074051
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # We vermenigvuldigen de input met 100 en maken daar een float van en daarna een integer zodat we er mee kunnen rekenen
paid = int(float(input('Paid amount: ')) * 100) # zelfde uitleg als hier boven
change = paid - toPay # wisselgeld is wat er is betaald min het bedrag dat moest betaald worden
aantal_wisselgeld = '' # lege string om te kunnen werken met een variable die later komt


if change > 0: 
  coinValue = 500 # altijd als er wisselgeld nodig is is de coinvalue altijd 500 cent
  
  while change > 0 and coinValue > 0: 
    nrCoins = change // coinValue  # wisselgeld delen door value van de coin en dit word altijd gedaan omdat change altijd groter is dan 0 en coinvalue ook ( tenzij er gepast word betaald)
    
    if nrCoins > 0: 
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # geeft de casierre aan met hoeveel hij/ zij terug moet geven van een bepaalde munt
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # hoeveel de casierre terug heeft gegeven
      change -= nrCoinsReturned * coinValue # change word steeds minder door het aantal coins teruggegeven * het soort coin te doen en dat van het change bedrag eraf halen
      aantal_wisselgeld += (f'{nrCoinsReturned} of {coinValue} \n') # het lijstje met het wisselgeld sla ik op na elke keer dat de cassiere iets invult en print ik aan het einde in een lijstje
      
      
    
# comment on code below: hier gaat hij langs elke coin
    
    if coinValue == 500: # als coinvalue gelijk is aan 500, word de volgende coinvalue 200
      coinValue = 200 # ^
    elif coinValue == 200: # precies zelfde als bij de if hierboven de cijfers worden alleen maar lager
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als wisselgeld groter is dan 0 na alle munten voorbij zijn.;
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done') # als hierboven niet het geval is print hij done

print(aantal_wisselgeld) # ik print het gene wat ik bij regel 23 heb gedaan 
