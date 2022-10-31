vraag_iphone = 'Hoe duur is de Iphone telefoon ?'
vraag_samsung = 'Hoe duur is de Samsung telefoon ?'

antwoord_iphone = int(input(vraag_iphone))
antwoord_samsung =int(input(vraag_samsung))
verschil_samsung_iphone = antwoord_iphone - antwoord_samsung

if verschil_samsung_iphone > 50:
    print(f'De iphone kost u {antwoord_iphone} en is meer dan 50 euro duurder dan de Samsung. Als advies geven we je mee dat je beter de Samsung kunt kopen.')

if verschil_samsung_iphone < 50:
    print(f'de iphone kost u {antwoord_iphone} en is niet meer dan 50 euro duurder dan de Samsung. We raden u aan om de Iphone te kopen')
    
if antwoord_samsung > antwoord_iphone:
    print(f'de Samsung kost u {antwoord_samsung} en is duurder dan de Iphone. Als advies geven we je mee dat je beter de Iphone kunt kopen.') 

if antwoord_iphone == antwoord_samsung + 50:
    print(f'de iphone kost u {antwoord_iphone} en is niet meer dan 50 euro duurder dan de Samsung. We raden u aan om de Iphone te kopen')
    
