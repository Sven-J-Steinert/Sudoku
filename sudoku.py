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

def get_block(z,s):

    # alle kleinen Blöcke
    case = {1 : A[0:3,0:3],
            2 : A[0:3,3:6],
            3 : A[0:3,6:9],

            4 : A[3:6,0:3],
            5 : A[3:6,3:6],
            6 : A[3:6,6:9],

            7 : A[6:9,0:3],
            8 : A[6:9,3:6],
            9 : A[6:9,6:9],
            }

    # Zuweisung des richtigen Blockes
    if (0 <= s < 3) and (0 <= z < 3): A_block = case[1]
    if (0 <= s < 3) and (3 <= z < 6): A_block = case[2]
    if (0 <= s < 3) and (6 <= z < 9): A_block = case[3]

    if (3 <= s < 6) and (0 <= z < 3): A_block = case[4]
    if (3 <= s < 6) and (3 <= z < 6): A_block = case[5]
    if (3 <= s < 6) and (6 <= z < 9): A_block = case[6]

    if (6 <= s < 9) and (0 <= z < 3): A_block = case[7]
    if (6 <= s < 9) and (3 <= z < 6): A_block = case[8]
    if (6 <= s < 9) and (6 <= z < 9): A_block = case[9]

    print(A_block)
    return A_block


def check_cell(z,s):
    print('')
    print('z (zeile): ', end='')
    print(z)
    print('s (spalte): ', end='')
    print(s)

    zahl_block = get_block(z,s)

    for i in range(0,9):
        zahl_zeile = A[z,i]
        zahl_spalte = A[i,s]

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
for s in range(0,9):
    # Zeilen
    for z in range(0,9):
        # für eine Zelle
        check_cell(z,s)












# eingeschränke Lösungsmenge
print(lsgmenge)
