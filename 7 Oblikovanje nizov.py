#F-NIZI!!!!
x = 20.67
y = 2

f"{x:4.1f} , {y + (100/2)}"

#Spremenljivke in izrazi so v {}
#po temu, je dvopicje(:) 
#po dvopicju pa lahko dolocimo stevilo mest in decimalk za spremenljivko(4.1 - 4 za stevilski del, 1 za decimalni del)

f"{x:.>10} , {y + (100/2):<3%}"

#< ali > pove, na katero stran so poravnani izpisi, % oblikuje izpis kot procent    

#primer vsega skupaj:
sk_voz = sum(voznje.values())
sk_raz = sum(razdalje.values())
sk_vis = sum(visine.values())

print()
print(f"{'Kolo':6}{'Število voženj':>19}{'Razdalja':>19}{'Višina':>19}")
print("-" * (6 + 3 * 19))
for kolo in voznje:
    voz, raz, vis = voznje[kolo], razdalje[kolo], visine[kolo]
    print(f"{kolo:12}{voz:5} ({voz / sk_voz:>5.1%}) {raz:10} "
          f"({raz / sk_raz:>5.1%}) {vis:10} ({vis / sk_vis:>5.1%})")
print("-" * (6 + 3 * 19))

#izpis:
Kolo       Število voženj           Razdalja             Višina
---------------------------------------------------------------
Canyon         26 (26.0%)       2766 (39.6%)      26392 (27.0%)
Cube           43 (43.0%)       3174 (45.4%)      66705 (68.3%)
Nakamura       22 (22.0%)        439 ( 6.3%)       1119 ( 1.1%)
Stevens         9 ( 9.0%)        607 ( 8.7%)       3395 ( 3.5%)
---------------------------------------------------------------



