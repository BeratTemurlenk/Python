a = 'Jan'
b = 'Umut'
c = 'Yassine'

if a == 'Jan'or b == 'Jan' or c == 'Jan':
    print('Het feest gaat door')
else: 
    print('Het feest gaat niet door')


a = 'emin'
b = 'klaas'
c = 'Menno'

if a == 'Jan' and (b == 'Umut' or c == 'Yasinne'):
    print('Het feest gaat door')
else: 
    print('Het feest gaat niet door')

def getBool(letter: str) -> bool:
    print(letter)
    if letter == 'a':
        return True
    elif letter == 'b':
        return True
    elif letter == 'c':
        return False
