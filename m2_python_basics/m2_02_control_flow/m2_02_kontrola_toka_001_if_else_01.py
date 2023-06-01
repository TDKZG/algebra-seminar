"""
MODUL       Modul 2 - Osnove programiranja u Pythonu
TEMA        Kontrola toka izvrsavanja programskog koda
NASLOV      Uvjetno izvrsavanje programa
            IF ELIF ELSE
"""


prvi_uvjet = False
drugi_uvjet = False
treci_uvjet = True
cetvrti_uvjet = True


if prvi_uvjet:
    print("Zadovoljen je prvi uvjet")
elif drugi_uvjet:
    print("Zadovoljen je drugi uvjet")
elif treci_uvjet:
    print("Zadovoljen je treci uvjet")
elif cetvrti_uvjet:
    print("Zadovoljen je cetvrti uvjet")
else:
    print("Nije zadovoljen niti jedan uvjet")


for broj in range(1, 31):
    if broj % 3 == 0:
        print(f"Broj {broj} je djeljiv s 3")

    if broj % 6 == 0:
        print(f"Broj {broj} je djeljiv s 6")

    if broj % 9 == 0:
        print(f"Broj {broj} je djeljiv s 9")
    else:
        print(f"Broj {broj} NIJE djeljiv s 3, 6 i 9")


for broj in range(1, 31):
    if broj % 3 == 0:
        if broj % 6 == 0:
            if broj % 9 == 0:
                print("Brojevi su djeljivi s 3, 6 i 9")
    else:
        print(f"Broj {broj} nije djeljiv s 3, 6 ili 9")


brojevi_djeljivi_s_3 = []
brojevi_djeljivi_sa_6 = []
brojevi_djeljivi_s_9 = []

for broj in range(1, 31):
    if broj % 3 == 0:
        brojevi_djeljivi_s_3.append(broj)
    if broj % 6 == 0:
        brojevi_djeljivi_sa_6.append(broj)
    if broj % 9 == 0:
        brojevi_djeljivi_s_9.append(broj)

print("Brojevi djeljivi s 3 :", brojevi_djeljivi_s_3)

print("Brojevi djeljivi sa 6:", brojevi_djeljivi_sa_6)

print("Brojevi djeljivi s 9:", brojevi_djeljivi_s_9)


for broj in range(1, 31):
    if broj % 3 == 0 and broj % 6 == 0 and broj % 9 == 0:
        print(broj)


for broj in range(1, 31):
    if broj % 3 != 0:
        print(f"Broj {broj} nije djeljiv s 3")
    elif broj % 6 != 0:
        print(f"Broj {broj} nije djeljiv s 6")
    elif broj % 9 != 0:
        print(f"Broj {broj} nije djeljiv s 9")
    else:
        print(f"Broj {broj} je djeljiv s 3, 6 i 9")
