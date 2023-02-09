
def fibo_lijst(fibo_lijst1, vraag,) -> int:

    
    
    getal_1 = fibo_lijst1[-1]
    getal_2 = fibo_lijst1[-2]
    antwoord = getal_1 + getal_2
    fibo_lijst1.append(antwoord)
    
    print(fibo_lijst1)
    
    
    if len(fibo_lijst1) <= vraag_getal:
        return(fibo_lijst(fibo_lijst1, vraag))
    return(fibo_lijst1)


start = [0, 1]
vraag_getal = int(input('geef een getal!'))
 


gulden_snede = fibo_lijst(start, vraag_getal,)
print(gulden_snede)


