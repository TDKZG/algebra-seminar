"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              ZADATAK WHILE i IF PETLJE
"""

### KAMEN ŠKARE PAPIR ###
import random

# Možemo i ovako definirati varijablu tekst
izbornik = """
    Izbornik opcija (upišite broj ispred opcije):
    0 - izlaz iz igre
    1 - Kamen
    2 - Škare
    3 - Papir
"""

brojac_korisnik = 0
brojac_racunalo = 0

print()
print("Dobrodosli u igru kamen, skare, papir")
print("-" * 35)
print(izbornik)
print("-" * 35)

while True:
    izbor_racunala = random.randint(1, 3)
    print()
    print("*" * 50)
    print(f"Rezultat - korisnik: {brojac_korisnik}, racunalo: {brojac_racunalo}")
    print("*" * 50)
    print()

    izbor_korisnika = int(input("Upisite jednu od opcija iz izbornika:\t"))
    if izbor_korisnika == izbor_racunala:
        print("NERIJEŠENO! Izabrali se isto kao i računalo")
    elif izbor_korisnika == 1 and izbor_racunala == 3:
        print("IZGUBILI ste, računalo je odabralo papir, a vi kamen")
        brojac_racunalo += 1
    elif izbor_korisnika == 1 and izbor_racunala == 2:
        print("POBIJEDILI ste, računalo je odabralo škare, a vi kamen")
        brojac_korisnik += 1
    elif izbor_korisnika == 3 and izbor_racunala == 2:
        print("IZGUBILI ste, računalo je odabralo škare, a vi papir")
        brojac_racunalo += 1
    elif izbor_korisnika == 3 and izbor_racunala == 1:
        print("POBIJEDILI ste, računalo je odabralo kamen, a vi papir")
        brojac_korisnik += 1
    elif izbor_korisnika == 2 and izbor_racunala == 1:
        print("IZGUBILI ste, računalo je odabralo kamen, a vi kamen")
        brojac_racunalo += 1
    elif izbor_korisnika == 2 and izbor_racunala == 3:
        print("POBIJEDILI ste, računalo je odabralo papir, a vi škare")
        brojac_korisnik += 1
    elif izbor_korisnika == 0:
        break
    else:
        print("Pogresan unos, molim vas upisite broj izmedu 0 i 3")

print("Hvala na igranju, nadam se da ste se zabavili")
