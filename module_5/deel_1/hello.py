vraag = int(input('hoeveel?'))


def geef_hello_terug (aantal: int):
    antwoord = ''
    for x in range(1,aantal + 1):
        antwoord += f'Hello from function town {x} \n'
    return antwoord



print(geef_hello_terug(vraag))
