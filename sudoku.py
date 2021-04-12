import numpy as np
#A = np.zeros( (9, 9) )
A = np.array([[0, 3, 0, 0, 0, 0, 0, 0, 0,],
             [0, 0, 0, 1, 9, 5, 0, 0, 0,],
             [0, 0, 8, 0, 0, 0, 0, 6, 0,],
             [8, 0, 0, 0, 6, 0, 0, 0, 0,],
             [4, 0, 0, 8, 0, 0, 0, 0, 1,],
             [0, 0, 0, 0, 2, 0, 0, 0, 0,],
             [0, 6, 0, 0, 0, 0, 2, 8, 0,],
             [0, 0, 0, 4, 1, 9, 0, 0, 5,],
             [0, 0, 0, 0, 0, 0, 0, 7, 0,]])
print(A)
#print(A[0,1])

B = A

lsgmenge = ['1','2','3','4','5','6','7','8','9']
print(lsgmenge)

# Zeile
for i in range(1,9):
    zahl = A[0,i]
    if zahl != 0:
        lsgmenge.remove(str(zahl))


print(lsgmenge)
