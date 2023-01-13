
def tafel_getal (aantal: int) -> str:
    for x in range(1,11):
        print(f'{x} x {aantal} = {x * aantal}')

tafel = int(input('Van welk getal wilt u de tafel zien?'))
tafel_getal(tafel)