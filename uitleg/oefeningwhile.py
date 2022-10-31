while True:
    try: 
        leeftijd = int(input("Hoe oud bent u?"))
        break
    except ValueError:
        print("Je moet wel cijfers intikken, probeer opnieuw.")


if leeftijd > 20:
    print("U bent aangenomen.")
else:
    print("U bent niet aangenomen.")