import numpy as np
from collections import Counter

dif = input('wähle einfach [1] oder schwer [2]: ')
# einfach
if dif == '1':
    A = np.array([[0, 0, 2, 6, 0, 0, 7, 0, 1, ],
                  [6, 8, 0, 0, 7, 0, 0, 9, 0, ],
                  [1, 9, 0, 0, 0, 4, 5, 0, 0, ],
                  [8, 2, 0, 1, 0, 0, 0, 4, 0, ],
                  [0, 0, 4, 6, 0, 2, 9, 0, 0, ],
                  [0, 5, 0, 0, 0, 3, 0, 2, 8, ],
                  [0, 0, 9, 3, 0, 0, 0, 7, 4, ],
                  [0, 4, 0, 0, 5, 0, 0, 3, 6, ],
                  [7, 0, 3, 0, 1, 8, 0, 0, 0, ]])


# schwer
if dif == '2':
    A = np.array([[0, 3, 0, 0, 0, 0, 0, 0, 0,],
                  [0, 0, 0, 1, 9, 5, 0, 0, 0,],
                  [0, 0, 8, 0, 0, 0, 0, 6, 0,],
                  [8, 0, 0, 0, 6, 0, 0, 0, 0,],
                  [4, 0, 0, 8, 0, 0, 0, 0, 1,],
                  [0, 0, 0, 0, 2, 0, 0, 0, 0,],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0,],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5,],
                  [0, 0, 0, 0, 0, 0, 0, 7, 0,]])

if dif != '1' and dif != '2':
    print('Ungültige Eingabe')
    exit(0)

print(A)
print('')


# Anfangslösungsmenge Klasse
class LSG:
    def __init__(self):
        self.value = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# Objektliste der Anfangslösungsmengen
objs = list()
for i in range(81):
    objs.append(LSG())


def print_lsgmenge():
    for i in range(81):
        print(i, end=' ')
        if len(objs[i].value) == 1:
            print('solved.', end=' ')
        else:
            print('        ', end='')
        print(objs[i].__dict__)
    print('')


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


# reduziere die Lösungsmengen bei den gegebenen Werte
# Spalte
for s in range(0, 9):
    # Zeilen
    for z in range(0, 9):
        # für eine Zelle
        if A[s, z] != 0:
            objs[9 * s + z].value = [str(A[s, z])]


# print_lsgmenge()


def get_block(z, s):
    # alle kleinen Blöcke
    case = {1: A[0:3, 0:3],
            2: A[0:3, 3:6],
            3: A[0:3, 6:9],

            4: A[3:6, 0:3],
            5: A[3:6, 3:6],
            6: A[3:6, 6:9],

            7: A[6:9, 0:3],
            8: A[6:9, 3:6],
            9: A[6:9, 6:9],
            }

    # Zuweisung des richtigen Blockes
    if (0 <= s < 3) and (0 <= z < 3):
      a_block = case[1]
    if (0 <= s < 3) and (3 <= z < 6):
      a_block = case[2]
    if (0 <= s < 3) and (6 <= z < 9):
      a_block = case[3]

    if (3 <= s < 6) and (0 <= z < 3):
      a_block = case[4]
    if (3 <= s < 6) and (3 <= z < 6):
      a_block = case[5]
    if (3 <= s < 6) and (6 <= z < 9):
      a_block = case[6]

    if (6 <= s < 9) and (0 <= z < 3):
      a_block = case[7]
    if (6 <= s < 9) and (3 <= z < 6):
      a_block = case[8]
    if (6 <= s < 9) and (6 <= z < 9):
      a_block = case[9]


    #print(A_block)
    return a_block



def check_cell(z,s,list):
    #print('')
    #print('z (zeile): ', end='')
    #print(z)
    #print('s (spalte): ', end='')
    #print(s)


    # hole passenden Block und forme ihn zu einer Liste
    block = get_block(z, s).reshape(1, 9)[0]

    # Wert der aktuellen Zelle
    cell = str(A[s, z])

    # nur wenn Feld noch nicht bekannt
    if cell == '0':

        for i in range(0, 9):
            zahl_zeile = A[s, i]
            zahl_spalte = A[i, z]
            zahl_block = block[i]

            # prüfe Zeile
            if zahl_zeile != 0 and (str(zahl_zeile) in list):
                list.remove(str(zahl_zeile))

            # prüfe Spalte
            if zahl_spalte != 0 and (str(zahl_spalte) in list):
                list.remove(str(zahl_spalte))

            # prüfe Block
            if zahl_block != 0 and (str(zahl_block) in list):
                list.remove(str(zahl_block))


for n in range(0, 81):
    # Spalte
    for s in range(0, 9):
        # Zeilen
        for z in range(0, 9):
            # für eine Zelle
            check_cell(z=z, s=s, list=objs[9 * s + z].value)

    # print_lsgmenge()

    # schreibe Lösung in Feld
    for s in range(0, 9):
        # Zeilen
        for z in range(0, 9):
            x = s * 9 + z
            if len(objs[x].value) == 1:
                for y in objs[x].value:
                    value = int(y)
                A[s, z] = value
    print('')
    print(A)

# vervollständigen

for i in range(0, 9):

    # zähle Zeile
    ges_z = list()
    for j in range(0, 9):
        ges_z.append(objs[i * 9 + j].value)
    anzahl_liste = Counter(flatten_list(ges_z))
    print(anzahl_liste)
    for c in range(1,10):
        if anzahl_liste[str(c)] == 1 :
            print(str(c) + ' nur einmal')
    print('')
    ges_z = 0

    # zähle Spalte

    # zähle Block

# eingeschränke Lösungsmenge
# print_lsgmenge()
print('end.')
