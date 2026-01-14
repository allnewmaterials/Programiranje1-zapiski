#Metoda branja1: po vrsticah 
for vrstica in open(path):
    #METODE NIZOV:
    x, y, z = vrstica.split(",") # splitta po vejici
    #(default po presledku). vrne samo stringe, zato 
    # moras po potrebi narediti int() ali float()
    vrstica.strip(".") # odstrani vstavljen znak iz leve in desne strani niza(default presledek)
    vrstica.lstrip().rstrip() #strippa samo levo/desno
    vrstica.lower().upper() #spremeni cel niz v velike/male crke
    vrstica.capitalize() # Poveca samo prvo crko v nizu 
    vrstica.replace("asd", "sda") # zamenja vse podnize "asd" z nizi "sda"
    vrstica.startswith("a") # preveri ce se zacne na podan niz (vrne true ali false)
    vrstica.endswith("a") #kj misls


#Metoda 2:
f = open("kolesa-z-glavo.txt")
f.read() #vrne en string vseh vrstic:
#'kolo,razdalja,višina,lastnik,leto nakupa\nCube,5031,159,Janez,2017\nStevens,3819,1284,Ana,2012\nFocus,3823,1921,Benjamin,2019'

f.readlines() #vrne seznam vrstic:
#['kolo,razdalja,višina,lastnik,leto nakupa\n',
# 'Cube,5031,159,Janez,2017\n',
# 'Stevens,3819,1284,Ana,2012\n',
# 'Focus,3823,1921,Benjamin,2019']

f.readline() #vrne samo eno vrstico:
#'kolo,razdalja,višina,lastnik,leto nakupa\n'

#Najuporabnejsi sta readline in read
#readline() bomo uporabili, kadar datoteka nima "homogenega" formata: različne vrstice imajo, recimo, različen pomen
#in praktično nam jih je brati eno za drugo.