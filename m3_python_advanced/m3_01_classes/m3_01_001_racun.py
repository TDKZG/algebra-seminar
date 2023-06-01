"""
MODUL               Modul 3 - Programiranje u Pythonu
TEMA                Korisnicki definirani tipovi podataka
NASLOV              Primjer RACUN
"""

import os

# racun_broj = "R-1-2023-02"
# racun_datum_izdavanja = "8.2.2023."
# racun_stavke = {
#     "Laptop": 500,
#     "Torba za laptop": 4.99,
#     "Monitor": 150,
# }
# racun_ukupan_iznos = 0
# for value in racun_stavke.values():
#     racun_ukupan_iznos += value

# racun_iznos_pdv = racun_ukupan_iznos * 0.25


# # ispis racuna
# print("*" * 50)
# print(f"\n\tRacun: {racun_broj}")
# print(f"\tDatum: {racun_datum_izdavanja}\n")
# print("-" * 50)
# print("\tProizvod\t\tCijena")
# print()
# for proizvod, cijena in racun_stavke.items():
#     print(f"\t{proizvod}\t\t{cijena}EUR")
# print()
# print("-" * 50)
# print(f"\tIznos PDV-a:\t{racun_iznos_pdv}")
# print(f"\tUkupan iznos:\t{racun_ukupan_iznos}")
# print("*" * 50)
# print()

import datetime

racuni = {}


def kreiraj_novi_racun():
    racun_broj = input("Unesi broj racuna: ")
    racun_datum_izdavanja = datetime.datetime.now()

    racun_stavke = {}
    while True:
        stavka = input("Unesi stavku: ")
        cijena = float(input("Unesi cijenu stavke: "))
        racun_stavke[stavka] = cijena

        odgovor = input("Upisi 0 za izlaz 1 za nastavak dodavanja stavki: ")
        if odgovor == "0":
            break

    racun_ukupan_iznos = 0
    for value in racun_stavke.values():
        racun_ukupan_iznos += value
    racun_iznos_s_pdvom = racun_ukupan_iznos * 1.25

    racuni[racun_broj] = [
        racun_datum_izdavanja,
        racun_stavke,
        racun_ukupan_iznos,
        racun_iznos_s_pdvom,
    ]

    return racun_broj


def ispis_racuna(racun_broj):
    trazeni_racun = racuni[racun_broj]
    racun_datum_izdavanja = trazeni_racun[0]
    racun_stavke = trazeni_racun[1]
    racun_ukupan_iznos = trazeni_racun[2]
    racun_iznos_s_pdvom = trazeni_racun[3]

    # ispis racuna
    print("*" * 50)
    print(f"\n\tRacun: {racun_broj}")
    print(f"\tDatum: {racun_datum_izdavanja}\n")
    print("-" * 50)
    print("\tProizvod\t\tCijena")
    print()
    for proizvod, cijena in racun_stavke.items():
        print(f"\t{proizvod}\t\t{cijena}EUR")
    print()
    print("-" * 50)
    print(f"\tIznos PDV-a:\t{racun_iznos_s_pdvom}")
    print(f"\tUkupan iznos:\t{racun_ukupan_iznos}")
    print("*" * 50)
    print()
    input("Pritisni neku tipku za nastavak")


while True:
    os.system("clear")
    racun_broj = kreiraj_novi_racun()
    ispis_racuna(racun_broj)
