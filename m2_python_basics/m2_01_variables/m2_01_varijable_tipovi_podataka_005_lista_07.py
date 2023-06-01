"""
MODUL               Modul 2 - Osnove programiranja u Pythonu
TEMA                Varijable i tipovi podataka
NASLOV              KOLEKCIJE PODATAKA
                    OSTALE naredbe za manipulaciju listama
"""


brojevi = []
for broj in range(0, 21):
    brojevi.append(broj)

brojevi.append(15)
print(brojevi)

print()

brojevi.clear()

brojevi_kopija = brojevi.copy()


brojevi_count = brojevi.count(15)
print("Broj pojavljivanja broja 15 u listi je:", brojevi_count)


rijeci = ["Python", "Algebra", "Programiranje"]

brojevi.extend(rijeci)
print(brojevi)


index_elemenenta = brojevi.index(15)
print(index_elemenenta)


brojevi.insert(0, "Ovo")
print(brojevi)


brojevi.sort()
print(brojevi)


brojevi.reverse()
print(brojevi)
