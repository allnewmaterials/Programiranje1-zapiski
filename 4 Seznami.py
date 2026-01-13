seznam = ["Ana", "Berta", "Cilka", "Dani"]

seznam.append("neki") # dodajanje na konec seznama


max(seznam) # vrne najvecnjo vrednost v seznamu
min(seznam)
sum(seznam)

len(seznam) # vrne stevilo elementov v seznamu 

"Cilka" in seznam
"Cilka" not in seznam
seznam3 = ["Ana", "Berta"]
if seznam3 in seznam:
    print("eden od elem. v prvem je v drugem")

seznam2 = [1,2,3]
x,y,z = seznam2

imena = ["Ana", "Berta", "Cilka", "Dani"]
teze = [57, 66, 58, 52]
for ime, teza in zip(imena, teze): 
    print(ime + ":", teza)
#zip(seznam) ustvari seznam parov iz dveh enako dolgih seznamov

dan = 0
temp = [5, 4, -1, -6, -8]
for dan, temp in enumerate(temperature):
    print(dan, ". december:", temp)
#enumerate kot argument prejme seznam ali poljubno 
#drugo stvar, prek katere je možno nagnati zanko for,
#recimo datoteko, slovar, niz... enumerate vrača pare
#(zaporedna številka, element)

#INDEKSIRANJE
seznam[4] # Steje od 0, indeks 4 je peti element
# POMEMBNO: len() vrne stevilko, ki je za 1 vecja od indeksa zadnjega elementa
seznam[-1] # zadnji indeks
seznam[-2] #predzadnji indeks

#REZINE - vkljuci spodnjo mejo, zgornje pa ne
seznam[5:8] #od petega do osmega elementa
seznam[:5] # prvih 5  
seznam[5:] #brez prvih 5
seznam[-3:] #zadnje 3
seznam[:-3] #brez zadnjih 3