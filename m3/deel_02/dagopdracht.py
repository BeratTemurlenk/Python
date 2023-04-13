dagen_van_de_week = ["1 = maandag" , "2 = dinsdag" , "3 = woensdag" ,  "4 = donderdag" ,  "5 = vrijdag" ,  "6 = zaterdag" ,  "7 = zondag"]
print("1 = maandag" , "2 = dinsdag" , "3 = woensdag" ,  "4 = donderdag" ,  "5 = vrijdag" ,  "6 = zaterdag" ,  "7 = zondag")
dag_vraag = int(input('welke dag is het? in cijfers'))


x = 0
while dag_vraag > x:
    print(dagen_van_de_week[x])
    x = x + 1
