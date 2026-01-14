import numpy as np

a = np.array([3, 8, 9, 2]) # tako se ustvari np array
b = np.array([8, 0, 1, -3])

a + b
#array([11,  8, 10, -1])
a - b
a * b
a + 1
b > 0
#array([ True, False,  True, False])
np.abs(b)
#array([8, 0, 1, 3])
np.sqrt(a)
np.sum(a)
np.max(a)

#Vektorske operacije

b[b > 0]
#array([8, 1])

np.sum(b[b > 0])
#9

#primer: st. pozitivnih elementov
np.sum(b > 0)

np.any(b > 0)

a[a % 2 == 0] #vrne soda stevila v seznamu

#PRIMER: visinska razlika
h = np.array([345, 355, 360, 364, 378, 370, 360, 355, 360, 361, 345])
d = h[1:] - h[:-1]
print(np.max(d))
print(np.sum(d[d > 0]))
#vec primerov na demsarjevih zapiskih

#VECDIMENZIONALNE TABELE

a = np.array([[2, -7, 2], [5, 9, 1], [1, -0, 0], [-1, -2, -8]])
a[3][2] #dostopanje, prvi[] pomeni kateri seznam v seznamu in drugi[] pa kateri element v notranjem seznamu
a[:, 2] #tudi rezine delujejo
a.T #stolpci postanejo vrstice, vrstice postanjeo stolpci
#array([[ 2, -7,  2],
#       [ 5,  9,  1],
#       [ 1,  0,  0],
#       [-1, -2, -8]])
#Spremenjeno:
#array([[ 2,  5,  1, -1],
#       [-7,  9,  0, -2],
#       [ 2,  1,  0, -8]])

np.zeros((2, 4)) # ustvari seznam poln nicel(float)
#array([[0., 0., 0., 0.],
#      [0., 0., 0., 0.]])
np.ones((2, 4)) # enke (float)
np.full((2, 4), 42) #poljubno st, v tem primeru 42

#lastnosti 2d tabele
a.ndim # stevilo dimenzij, v tem primeru vrne 2
a.shape # dimenzije tabele, tukaj vrne (4, 3)
a.dtype # tip spremenljivk v tabeli, tukaj dtype('int64')

#spreminjanje lastnosti tabele

b = a.reshape(2, 6)
#array([[ 2, -7,  2,  5,  9,  1],
#       [ 1,  0,  0, -1, -2, -8]])

a.astype(float) #spremeni tip spremenljivk v seznamu

#OSI
#2d tabele imata 2 osi (horizontalna(axis=0) in vertikalna(axis=1))
np.max(a, axis=0) #najvecje vrednosti po x osi 
#array([5, 9, 2])

np.max(a, axis=1) #najvecje vrednosti po y osi
#array([ 2,  9,  1, -1])

np.sum(a, axis=0)


