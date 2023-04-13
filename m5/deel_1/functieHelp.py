def get_float_int(vraag: str):
    while True:
        vraag_getal = input(vraag)
        try:
            getal = float(vraag_getal)
            break
        except ValueError:
            print('voer getal 1 in')
    return getal










