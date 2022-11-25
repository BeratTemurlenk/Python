string1 = 'PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm'
next = False
decrypted_zin = " "

for x in string1:
    
    
    if next:
        decrypted_zin += x 
        next = False 
    
    
    vraagteken_gevonden = x == '?'
    next = vraagteken_gevonden and uitroepteken_gevonden
    uitroepteken_gevonden = x == "!"

    
print(decrypted_zin)
        
    
       


