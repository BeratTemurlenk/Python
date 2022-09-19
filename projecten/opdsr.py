vraag = 'heet je jan?'
naam = input('naam?')
leeftijd = int(input('wat is je leeftijd?'))
input('naam?')
input('leeftijd?')
input('heet je jan?')

if leeftijd > 16:
    if naam == 'jan': 
        print('je mag naar binnen en je krijgt een gratis kaartje!')
    else: print('je mag naar binnen maar je krijgt geen gratis drankje')

elif leeftijd < 16:
    print('helaas mag je nog niet naar binnen') 


