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



