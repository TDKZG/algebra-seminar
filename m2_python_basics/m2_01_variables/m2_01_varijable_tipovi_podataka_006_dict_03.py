"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    DICTIONARY - rjecnik
                    DODATNE NAREDBE
"""


# help(dict)


vozni_park = {
    1: ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    2: ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    3: ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    4: ["Tegljač", "MAN", "RI 002 ZZ", 2020, 97000.00],
    5: ["Kombi", "Mercedes Benz", "ST 001 ZZ", 2013, 12000.00],
    6: ["Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00],
    7: ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    8: ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", 2010, 9300.00],
}

print()
print("Ispis PRIJE clear()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

vozni_park.clear()
print()

print("Ispis NAKON clear()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()


print("Ispis PRIJE pop()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

izbacena_vrijednost = vozni_park.pop(9, "Ne postoji trazeni element u bazi")
print()
print("izbacena vrijednost je: ", izbacena_vrijednost)
print()

print("Ispis POSLIJE pop()")
print()

for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

vozni_park["0"] = ["kamion", 100]

print("Ispis PRIJE popitem()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

item = vozni_park.popitem()
print()
print("vrijednost koju je vratio popitem", vrijednost)
print()

for broj in range(5):
    vozni_park.popitem()


print("Ispis POSLIJE popitem()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()


# JOS JEDAN POP

print("Ispis PRIJE pop()")
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()

print()
for broj in range(1, 4):
    vozni_park.pop(broj)

print("Ispis POSLIJE pop()")
print()
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")
    for element in vrijednost:
        print(f"{element}", end="\t")
    print()
