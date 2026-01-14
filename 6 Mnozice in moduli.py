import math
# math.pi, math.sin(x),...
from math import sin, cos, radians, pi
#pi, sin(x), radians(x),...
from math import *
#uvozis vse funkcije, tega rajs ne delat

#MATH MODUL
#inf
def min(s):
    m = math.inf
    for x in s:
        if x < m:
            m = x
    return m

math.nan #tega najbrs ne bomo nucal

#RANDOM
import random

random.random() # vrne "nakljucno" stevilo
random.uniform(10, 20) # "nakjlucno" stevilo med 10 in 20
random.choice(seznam) # vrne nakljucno vrednost iz seznama
random.sample(seznam, x) # vrne seznam x-tih nakljucnih vrednosti iz vhodnega seznama
random.choices(seznm, k=5) # podobno kot prejsen, samo da se vrednosti lahko ponavljajo (podano mora biti y k=...)

#OS
import os

getcwd() # vrne trenutni direktorij. Uporabno, ker nikoli ne ves kje si.
chdir(path) # spremeni trenutni direktorij. 
mkdir(path) # naredi nov direktorij
remove(filename) # pobriše datoteko s podanim imenom
rename(name, newname) # preimenuje datoteko.
listdir(path) # vrne seznam vseh imen datotek v podanem direktoriju.


os.path.exists(name) # vrne True, če (v trenutnem direktoriju) obstaja datoteka ali direktorij s podanim imenom.
os.path.isdir(name) # vrne True, če je podano ime direktorij (znotraj trenutnega direktorija).
os.path.isfile(name) # vrne True, če je podano ime datoteka (znotraj trenutnega direktorija).
os.path.splitext(name) # vrne osnovo in končnico podanega imena datoteke.

#PRIMER

#izpis vseh datotek s koncnico .txt v nekem direktoriju
for ime in os.listdir():
    osnova, koncnica = os.path.splitext(ime)
    if os.path.isfile(ime) and koncnica == ".txt":
        print(ime)

#COLLECTIONS - DEFAULT DICT
from collections import defaultdict

#definicija od demsarja:
#defaultdict je slovar, ki sproti dodaja neobstoječe ključe, podati pa mu moramo funkcijo, s katero si bo izmišljal njihove vrednosti. 
#Primerne so le funkcije, ki ne sprejemajo argumentov, oziroma, točneje, funkcije, ki jih lahko pokličemo (tudi) brez argumentov. Najpogosteje bo to int. 
#Če jo pokličemo brez argumentov namreč vrne 0.
d = defaultdict(int)

#okj tega najbrs ne bomo nucal

#CSV
import csv
#csv datoteke vsebujejo podatke, locene z vejicami, vrstice pa ostanejo.
for vrstica in csv.reader(open(ime_dat)): #csv.reader vrne seznam vrednosti, locene z vejico. lahko podamu tudi argument delimeter="-" in bo namesto po vejicah loceval po danemu znaku.
    print(vrstica)


#branje txt datoteke kot csv
ime_dat = "../domace-naloge/05-druzabno-omrezje-drazbe/kolesa.txt"
sniffer = csv.Sniffer()  # vrne novega "snifferja"
dialect = sniffer.sniff(open(ime_dat).read())  # preberemo vsebino datoteke in jo damo posniffati :)
for v in csv.reader(open(ime_dat), dialect):
    print(v)

#TIME, DATETIME, CALENDAR
import time

time.time() #cas v sekundah od 1.januar 1970 po greenwichu

zdaj = time.localtime() # 

print("Danes je ", zdaj.tm_mday, ". ", zdaj.tm_mon, ". ", zdaj.tm_year, ".", sep="")

# Danes je 10. 2. 2024.
#prolly ne rabmo vec

#
