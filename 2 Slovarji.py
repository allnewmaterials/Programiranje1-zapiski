slovar = {"kljuc":"par", "kljuc2":"par2"}
slovar["kljuc"] # dostopanje
slovar = {}

if "kljuc" in slovar:
    #to vrne true ali false, odvisno ce je ta kljuc v slovarju
    pass

if "kljuc" not in slovar:
    #ce ga ni
    pass

print(slovar.values()) # vrne array vseh vrednosti ["par", "par2"]

slovar.setdefault("neki", 0) # za podani kljuc nastavi podano vrednost in vrne vrednost. Ce ta kljuc ze obstaja in ima vrednost funkcija samo vrne trenutno vrednost 

for kljuc, vredost in slovar.items():
    # items vrne par kljuca in vrednosti. Uporabno za iteracijo cez slovar

for kljuc in slovar:
    # iterira samo cez kljuce