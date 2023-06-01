"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRSAVANJE PROGRAMA
                    BREAK i CONTINUE za FOR i WHILE petlje
"""

tekst = "Programiranje u Pythonu"

for znak in tekst:
    print(znak, end=" ")
print()

for znak in tekst:
    if znak == "t":
        break
    print(znak, end=" ")
print()


while True:
    print("Pozdrav iz potencijalno beskonacne WHILE petlje")

    odgovor = int(input("Zelite li prekinuti petlju? (Da=1/Ne=0) "))

    if odgovor == 1:
        print("Izlazimo iz petlje")
        break
    elif odgovor == 0:
        print("Ostajemo u petlji")
    else:
        print("Unijeli ste pogresan unos")

tekst = "Python programer"

for znak in tekst:
    if znak == "g":
        continue
    print(znak, end="")
print()

import random

izbor_racunala = random.randint(1, 3)
