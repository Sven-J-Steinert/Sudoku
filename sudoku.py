import numpy as np

A = np.array([[0, 3, 1, 0, 0, 0, 0, 0, 0,],
             [7, 6, 2, 1, 9, 5, 0, 0, 0,],
             [9, 5, 8, 0, 0, 0, 0, 6, 0,],
             [8, 0, 0, 0, 6, 0, 0, 0, 0,],
             [0, 0, 0, 8, 0, 0, 0, 0, 1,],
             [0, 0, 0, 0, 2, 0, 0, 0, 0,],
             [0, 6, 0, 0, 0, 0, 2, 8, 0,],
             [0, 0, 0, 4, 1, 9, 0, 0, 5,],
             [0, 0, 0, 0, 0, 0, 0, 7, 0,]])

#A_klein1 = A[0:3,0:3].reshape((1, 9))


#print(A_klein1)
print(A)

# Anfangslösungsmenge
lsgmenge = ['1','2','3','4','5','6','7','8','9']
print(lsgmenge)

def check_cell(z,s):
    for i in range(1,9):
        zahl_zeile = A[z,i]
        zahl_spalte = A[i,s]
        #zahl_block = A_klein1[0,i]
        # prüfe Zeile
        if zahl_zeile != 0 and (str(zahl_zeile) in lsgmenge):
            lsgmenge.remove(str(zahl_zeile))
        # prüfe Spalte
        if zahl_spalte != 0 and (str(zahl_spalte) in lsgmenge):
            lsgmenge.remove(str(zahl_spalte))
        # prüfe Block
        #if zahl_block != 0 and (str(zahl_block) in lsgmenge):
        #    lsgmenge.remove(str(zahl_block))


# für alle
# Spalte
for s in range(1,9):
    # Zeilen
    for z in range(1,9):
        # für eine Zelle
        check_cell(z,s)











# eingeschränke Lösungsmenge
print(lsgmenge)
