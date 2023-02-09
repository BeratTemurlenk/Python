
def fibo_lijst(fibo_lijst1, vraag,) -> int:

    
    for x in range(vraag_getal - 2):
        getal_1 = fibo_lijst1[-1]
        getal_2 = fibo_lijst1[-2]
        antwoord = getal_1 + getal_2
        fibo_lijst1.append(antwoord)

    if len(fibo_lijst1) >= vraag_getal:
        gulden_snede = antwoord / getal_2
        return gulden_snede

start = [0, 1]
vraag_getal = int(input('geef een getal!'))

gulden_snede = fibo_lijst(start, vraag_getal,)
print(gulden_snede)


