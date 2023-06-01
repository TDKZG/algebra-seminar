"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Kontrola toka izvršavanja programskog kôda
NASLOV              UVJETNO IZVRŠAVANJE PROGRAMA
                    IF ELIF ELSE ZADACI
"""


rijec = input("Upišite rijec za koju mislite da je PALINDROM:\t")

obrnuta_rijec = rijec[::-1]

if rijec == obrnuta_rijec:
    print(f"Riječ {rijec} JE palindrom.")
else:
    print(f"Riječ {rijec} NIJE palindrom.")


# Baza je rječnik. Evo primjera s podacima:
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

# HEADER TABLE ROW
print()
print("_" * 90)
header_top_line = "ID\tTip\t\tProizvodac\tRegistarska\t\tGodina prve\tCijena"
header_bottom_line = "  \t   \t\t          \toznaka\t\t\tregistracije\t(EUR)"
print(header_top_line, "\n", header_bottom_line)
print("_" * 90, "\n")

# BODY TABLE ROWs
for kljuc, vrijednost in vozni_park.items():
    print(f"{kljuc}", end="\t")

    for element in vrijednost:
        if type(element) == str:
            # Ako je tekst i dužina riječi je duža od 9 znakova.
            # koristimo jedan TAB.
            if len(element) > 9:
                print(f"{element}", end="\t")
            # INAČE koristimo dva taba
            else:
                print(f"{element}", end="\t\t")
        else:
            print(f"{element}", end="\t\t")

    print()  # I tek sada možemo preći u novi red
print("_" * 90, "\n\n")
