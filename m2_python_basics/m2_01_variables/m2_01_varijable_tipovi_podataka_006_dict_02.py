"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    DICTIONARY - rjecnik
                    ZADATAK
"""


vozni_park = {
    "sdfg1": ["Kamion", "Iveco", "OS 001 ZZ", 2015, 45000.00],
    "2gdf": ["Kamion", "Iveco", "OS 002 ZZ", 2015, 47000.00],
    "3hgfd": ["Tegljač", "MAN", "RI 001 ZZ", 2018, 78000.00],
    "4htr": ["Tegljač", "MAN", "RI 002 ZZ", 2020, 97000.00],
    "5ngf": ["Kombi", "Mercedes Benz", "ST 001 ZZ", 2013, 12000.00],
    "6nfgd": ["Kombi", "Volkswagen", "ST 002 ZZ", 2021, 35000.00],
    "7hrt": ["Dostavno vozilo", "Volkswagen", "ZG 001 ZZ", 2010, 9000.00],
    "8hty": ["Dostavno vozilo", "Volkswagen", "ZG 002 ZZ", 2010, 9300.00],
}


# HEADER ROW
# header_top_row = f"ID\tTip\t\tProizvodac\t\tRegistarska\t\tGodina prve\t\tCijena"
# header_bottom_row = f"  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)"
# header_line = "_" * 105
# print(header_top_row, header_bottom_row, header_line, sep="\n")


# # TABLE BODY
# brojac = 0
# lista_kljuceva = list(vozni_park.keys())
# while brojac < len(vozni_park):
#     kljuc = lista_kljuceva[brojac]
#     vrijednost = vozni_park[kljuc]
#     print(kljuc, end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t\t")
#     print()
#     brojac += 1


# for kljuc, vrijednost in vozni_park.items():
#     print(f"{kljuc}", end="\t")
#     for element in vrijednost:
#         print(f"{element}", end="\t\t")
#     print()


# header_top_row = f"ID\tTip\t\tProizvođač\t\tRegistarska\t\tGodina prve\t\tCijena"
# header_bottom_row = f"  \t   \t\t          \t\toznaka\t\t\tregistracije\t\t(EUR)"
# header_line = "_" * 100
# print(header_top_row, header_bottom_row, header_line, sep="\n")

