kassa.py

bedrag = float(input("Voer bedrag in: ")) * 100

aantal_twee_euro = bedrag // 200
print( "Aantal 2 euro: {}".format(aantal_twee_euro))
restant = bedrag - aantal_twee_euro * 200
aantal_een_euro = restant // 100
print(f"Aantal 1 euro: {aantal_een_euro}")
aantal_vijftig_cent = restant // 50
print(f"Aantal 50 eurocent: {aantal_vijftig_cent}")
aantal_twintig_cent = restant // 20
print(f"Aantal 20 eurocent: {aantal_vijftig_cent}")
aantal_tien_cent = restant // 10
print(f"Aantal 10 eurocent: {aantal_tien_cent}")